from dataclasses import dataclass
from datetime import datetime as dt
from datetime import timedelta

from sqlalchemy import CheckConstraint, Column, DateTime, String
from sqlalchemy.orm import validates

from app.configs.database import db
from app.exc import CpfFormatError, FieldTypeError


@dataclass
class VaccineCard(db.Model):
    cpf: str
    name: str
    first_shot_date: dt
    second_shot_date: dt
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_cards"

    cpf = Column(String, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime, nullable=False, default=dt.now())
    second_shot_date = Column(
        DateTime, nullable=False, default=(dt.now() + timedelta(days=90))
    )
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String, nullable=False)

    __table_args__ = (CheckConstraint(('length("cpf") = 11'), name="check_cpf"),)

    @validates("cpf", "name", "vaccine_name", "health_unit_name")
    def validate_field_type(self, key, value):

        if type(value) != str:
            raise FieldTypeError(key)

        if key == "cpf" and len(value) != 11:
            raise CpfFormatError

        return value.title()

    def __repr__(self) -> str:
        return f"{self.name} - [{self.vaccine_name}] - [{self.first_shot_date}] => [{self.second_shot_date}]"
