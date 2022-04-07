from http import HTTPStatus
from flask import request, jsonify
from app.configs.database import db
from sqlalchemy.orm.session import Session

from app.models.vaccine_model import Vaccine


def create_vaccine():
    data = request.get_json()

    vaccine = Vaccine(**data)

    session: Session = db.session
    session.add(vaccine)
    session.commit()

    serialized_call_record = {
        key: value
        for key, value in vaccine.__dict__.items()
        if key != "_sa_instance_state"
    }

    return jsonify(serialized_call_record), HTTPStatus.CREATED


def retrieve_vaccines():
    return {"get vacines"}
