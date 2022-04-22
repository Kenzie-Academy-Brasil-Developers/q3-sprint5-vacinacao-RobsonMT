from functools import wraps
from http import HTTPStatus
from typing import Callable

from flask import request

from app.exc.vaccine_card_exc import MissingKeyError, WrongkeyError

post_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]


def validate_fields(fields: list = post_keys):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            keys_missing = set(fields).difference(data.keys())
            wrong_keys = set(data.keys()).difference(fields)

            try:
                if wrong_keys:
                    raise WrongkeyError

                if keys_missing:
                    raise MissingKeyError

                return func(*args, **kwargs)

            except MissingKeyError:
                return {
                    "expected keys": fields,
                    "key(s) missing": list(keys_missing),
                }, HTTPStatus.BAD_REQUEST
            except WrongkeyError:
                return {
                    "expected keys": fields,
                    "key(s) error": list(wrong_keys),
                }, HTTPStatus.BAD_REQUEST

        return wrapper

    return decorator
