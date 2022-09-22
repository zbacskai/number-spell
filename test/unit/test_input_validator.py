import pytest

from number_spell.spell import _validate_input, InputValidationException


def test_input_validator_fail_on_non_digits():
    with pytest.raises(InputValidationException):
        _validate_input("10'000")


def test_input_validator_fail_on_coma():
    with pytest.raises(InputValidationException):
        _validate_input("100,00")


def test_input_validator_fail_on_dot():
    with pytest.raises(InputValidationException):
        _validate_input("100.00")


def test_input_validator_fail_on_space_in_middle():
    with pytest.raises(InputValidationException):
        _validate_input("100 00")


def test_input_validator_fail_on_space_in_beginning():
    with pytest.raises(InputValidationException):
        _validate_input(" 10000")


def test_input_validator_fail_on_space_in_end():
    with pytest.raises(InputValidationException):
        _validate_input("10000 ")


def test_input_validator_fail_on_number_out_of_range_upper():
    with pytest.raises(InputValidationException):
        _validate_input("100001")


def test_input_validator_fail_on_number_out_of_range_lower():
    with pytest.raises(InputValidationException):
        _validate_input("-1")


def test_input_validator_acceptable_range():
    try:
        for i in range(0, 100001):
            _validate_input(f'{i}')
    except InputValidationException:
        assert False, f"Input validator failed on {i} but it shouldn't."
