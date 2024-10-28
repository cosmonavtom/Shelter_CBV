import re
from django.core.exceptions import ValidationError


def validate_password(field):
    pattern = re.compile(r'^[A-Za-z0-9]+$')
    if not bool(re.match(pattern, field)):
        # print('Must contain A-Z, a-z letters and 0-9 numbers')
        raise ValidationError('Только латиница и цифры')
    if not 6 <= len(field) <= 12:
        # print('Password length must be between 6 and 12')
        raise ValidationError('Длина пароля от 6 до 12 символов')
