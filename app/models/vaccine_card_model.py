from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

from dataclasses import dataclass

from datetime import datetime as dt
from datetime import timedelta

from app.configs.database import db

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
    second_shot_date = Column(DateTime, nullable=False, default=(dt.now() + timedelta(days=90)))
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)

    __table_args__ = (CheckConstraint(('length("cpf") = 11'), name="check_cpf"),)

    def __repr__(self) -> str:
        return f"{self.name} - [{self.vaccine_name}]"