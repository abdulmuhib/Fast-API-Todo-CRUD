from re import match
from excetion_handling import ApiException


def validate_field(field_value, field_name, regex_pattern, max_length):
    if not match(regex_pattern, field_value) or len(field_value) > max_length:
        raise ApiException.value_error(
            f"Invalid {field_name}. {field_name} must match the pattern {regex_pattern} and can't be longer than {max_length} characters.")
