from curses import keyname
from http import HTTPStatus
from multiprocessing.sharedctypes import Value
from flask import request, jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query

from app.decorators.validate_fields import validate_fields
from app.models.vaccine_card_model import VaccineCard

from app.configs.database import db


@validate_fields()
def create_vaccine_card():
    data = request.get_json()

    new_data = {
        "cpf": data["cpf"],
        "name": data["name"],
        "vaccine_name": data["vaccine_name"],
        "health_unit_name": data["health_unit_name"]
    }

    try:
        vaccine_card = VaccineCard(**new_data)

        session: Session = db.session
        session.add(vaccine_card)
        session.commit()

        return jsonify(vaccine_card), HTTPStatus.CREATED

    except IntegrityError:
        return {"error": "cpf already exists"}, HTTPStatus.CONFLICT


def retrieve_vaccine_cards():
    base_query: Query = db.session.query(VaccineCard)

    vaccine_cards = base_query.all()

    return jsonify(vaccine_cards), HTTPStatus.OK
