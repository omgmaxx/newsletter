from django.core.exceptions import ValidationError


def validate_gmt(value) -> None:
    if not -12 <= value <= 14:
        raise ValidationError(f'{value} is not in GMT range (-12 to +14)')


def validate_phone_number(value) -> None:
    """Validates that phone number is integer and doesn't start with zeros"""
    try:
        val = int(value)
    except ValueError:
        raise ValidationError(f'{value} is not numeric value')

    if val < 100:
        raise ValidationError(f"{value}'s phone code starts with 0")