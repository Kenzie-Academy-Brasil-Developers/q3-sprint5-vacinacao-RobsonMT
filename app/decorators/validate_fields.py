from functools import wraps
from http import HTTPStatus
from typing import Callable
from flask import request

from app.exc.vaccine_card_exc import CpfFormatError
from app.exc.vaccine_card_exc import FieldTypeError
from app.exc.vaccine_card_exc import MissingKeyError

REQUIRED_FIELDS = ["cpf", "name", "vaccine_name", "health_unit_name"]


def validate_fields(fields: list = REQUIRED_FIELDS):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            missing_keys = [key for key in fields if key not in data.keys()]

            try:
                if missing_keys:
                    raise MissingKeyError(missing_keys)

                for key, value in data.items():

                    if type(value) != str: 
                        raise FieldTypeError(key)

                    if key == "cpf" and len(value) != 11: 
                        raise CpfFormatError
                      
                    data.update({key: value.title()})

                return func(*args, **kwargs)

            except MissingKeyError as err:
                return {"expected_keys": fields,"missing_key(s)": list(err.args[0])}, HTTPStatus.BAD_REQUEST
            except FieldTypeError as err:
                return {"error": f"the {err} must be a string."}, HTTPStatus.BAD_REQUEST
            except CpfFormatError:
                return {"error": "Key cpf should contains 11 characteres."}, HTTPStatus.BAD_REQUEST
               
        return wrapper

    return decorator
