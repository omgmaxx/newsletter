from django.core.exceptions import ValidationError


def validate_gmt(value):
    if not -12 <= value <= 14:
        raise ValidationError(f'{value} is not in GMT range (-12 to +14)')


def validate_phone_number(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError(f'{value} is not numeric value')