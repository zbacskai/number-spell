import pytest

from number_spell.spell import Period, _parse_periods, _translate_period_numbers, _translate_a_period, \
    _translate_periods


def test_period_valid_input_3_digits():
    p = Period(period_s='234', period_id=0)
    assert 2 == p.hundreds
    assert 34 == p.tens_and_ones
    assert 0 == p.period_id


def test_period_somewhat_valid_input_4_digits_only_lower_3_shall_be_parsed():
    p = Period(period_s='1234', period_id=0)
    assert 2 == p.hundreds
    assert 34 == p.tens_and_ones
    assert 0 == p.period_id


def test_period_valid_input_2_digits():
    p = Period(period_s='23', period_id=0)
    assert 0 == p.hundreds
    assert 23 == p.tens_and_ones
    assert 0 == p.period_id


def test_period_valid_input_1_digits():
    p = Period(period_s='4', period_id=0)
    assert 0 == p.hundreds
    assert 4 == p.tens_and_ones
    assert 0 == p.period_id


def test_period_invalid_valid_input_0_digits():
    with pytest.raises(ValueError):
        Period(period_s='', period_id=0)


def test_period_invalid_input_non_digits():
    with pytest.raises(ValueError):
        Period(period_s='1a3', period_id=0)


def test_period_parse_no_filter_of_zero_period():
    parsed_periods = _parse_periods('1234567')
    expected_periods = [Period('1', 2), Period('234', 1), Period('567', 0)]
    assert len(expected_periods) == len(parsed_periods)
    for i in range(0, 3):
        assert expected_periods[i].hundreds == parsed_periods[i].hundreds, f"Hundreds missmatch {i}"
        assert expected_periods[i].tens_and_ones == parsed_periods[i].tens_and_ones, f"Tens missmatch {i}"
        assert expected_periods[i].period_id == parsed_periods[i].period_id, f"Period id mismatch {i}"


def test_period_parse_filter_of_zero_period():
    parsed_periods = _parse_periods('1000567')
    expected_periods = [Period('1', 2), Period('567', 0)]
    assert len(expected_periods) == len(parsed_periods)
    for i in range(0, 2):
        assert expected_periods[i].hundreds == parsed_periods[i].hundreds, f"Hundreds missmatch {i}"
        assert expected_periods[i].tens_and_ones == parsed_periods[i].tens_and_ones, f"Tens missmatch {i}"
        assert expected_periods[i].period_id == parsed_periods[i].period_id, f"Period id mismatch {i}"


def test_period_parse_filter_of_zero_periods():
    parsed_periods = _parse_periods('1000000')
    expected_periods = [Period('1', 2)]
    assert len(expected_periods) == len(parsed_periods)
    for i in range(0, 1):
        assert expected_periods[i].hundreds == parsed_periods[i].hundreds, f"Hundreds missmatch {i}"
        assert expected_periods[i].tens_and_ones == parsed_periods[i].tens_and_ones, f"Tens missmatch {i}"
        assert expected_periods[i].period_id == parsed_periods[i].period_id, f"Period id mismatch {i}"


def test_period_parse_filter_all_zero_periods():
    parsed_periods = _parse_periods('00000000')
    expected_periods = []
    assert len(expected_periods) == len(parsed_periods)


def test_translate_period_numbers_hundreds_tens_and_ones():
    result = _translate_period_numbers(Period(period_s='643', period_id=0))
    assert result == 'six hundred and forty-three'


def test_translate_period_numbers_hundreds_only():
    result = _translate_period_numbers(Period(period_s='400', period_id=0))
    assert result == 'four hundred'


def test_translate_period_numbers_tens_and_ones_only():
    result = _translate_period_numbers(Period(period_s='17', period_id=0))
    assert result == 'seventeen'


def test_translate_period_only_ones():
    result = _translate_a_period(Period(period_s='411', period_id=0))
    assert result == 'four hundred and eleven'


def test_translate_period_thousands():
    result = _translate_a_period(Period(period_s='411', period_id=1))
    assert result == 'four hundred and eleven thousand'


def test_translate_periods_representing_number_coma_separator():
    result = _translate_periods([Period(period_s='1', period_id=1), Period(period_s='983', period_id=0)])
    assert result == 'one thousand, nine hundred and eighty-three'


def test_translate_periods_representing_number_and_separator():
    result = _translate_periods([Period(period_s='1', period_id=1), Period(period_s='001', period_id=0)])
    assert result == 'one thousand and one'

def test_translate_periods_empty_period_listr():
    with pytest.raises(IndexError):
        result = _translate_periods([])