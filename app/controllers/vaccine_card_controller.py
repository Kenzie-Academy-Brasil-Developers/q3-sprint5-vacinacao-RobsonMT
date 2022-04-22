from http import HTTPStatus

from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.decorators.validate_fields import validate_fields
from app.exc import CpfFormatError, FieldTypeError
from app.models.vaccine_card_model import VaccineCard


@validate_fields()
def create_vaccine_card():
    data = request.get_json()

    session: Session = db.session

    try:
        vaccine_card = VaccineCard(**data)

        session.add(vaccine_card)
        session.commit()

        return jsonify(vaccine_card), HTTPStatus.CREATED

    except IntegrityError:
        session.rollback()
        return {"error": "cpf already exists"}, HTTPStatus.CONFLICT
    except FieldTypeError as key:
        session.rollback()
        return {"error": f"the {key} must be a string!"}, HTTPStatus.BAD_REQUEST
    except CpfFormatError:
        session.rollback()
        return {
            "error": "Key cpf should contains 11 characteres."
        }, HTTPStatus.BAD_REQUEST
    finally:
        session.close()


def retrieve_vaccine_cards():
    session: Session = db.session

    vaccine_cards = session.query(VaccineCard).all()

    return jsonify(vaccine_cards), HTTPStatus.OK
