from flask import Blueprint

from app.controllers import vaccine_controller

bp = Blueprint("vaccine", __name__, url_prefix="/vaccine")

bp.get("")(vaccine_controller.create_vaccine)
bp.post("")(vaccine_controller.retrieve_vaccines)
