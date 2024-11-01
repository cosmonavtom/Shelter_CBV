import re

from django.conf import  settings
from django.core.exceptions import ValidationError


def validate_password(field):
    pattern = re.compile(r'^[A-Za-z0-9]+$')
    language = settings.LANGUAGE_CODE
    error_messages = [
        {
            'ru-ru': 'Только латиница и цифры',
            'en-us': 'Must contain A-Z, a-z letters and 0-9 numbers'
        },
        {
            'ru-ru': 'Длина пароля от 6 до 12 символов',
            'en-us': 'Password length must be between 6 and 12'
        }
    ]
    if not bool(re.match(pattern, field)):
        # print(error_messages[0][language])
        raise ValidationError(
            error_messages[0][language],
            code=error_messages[0][language]
        )
    if not 6 <= len(field) <= 12:
        # print(error_messages[1][language])
        raise ValidationError(
            error_messages[1][language],
            code=error_messages[1][language]
        )
