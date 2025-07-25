from django.core.exceptions import ValidationError
from constants import VALID_ROWS, VALID_SEATS

def is_valid_seat_code(seat_code: str) -> bool:
    try:
        row_str, seat_letter = seat_code.split('-')
        row = int(row_str)
        return row in VALID_ROWS and seat_letter.upper() in VALID_SEATS
    except (ValueError, AttributeError):
        return False

def validate_seat_format(value):
    if not is_valid_seat_code(value):
        raise ValidationError("Seat format should be XX-Y, where XX (row) = 1–20, Y (seat in a row) = A–Q")
