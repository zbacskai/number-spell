from number_spell.constants import ONES_MAP, TENS_AND_ONES_MAP, PERIOD_MAP
import re

INPUT_REGEX = re.compile(r"^0$|^[1-9][0-9]{0,4}$|^10{5}$")

ZERO_DIGIT_S = '0'


class InputValidationException(Exception):
    pass


def _validate_input(input_str: str):
    if not re.match(INPUT_REGEX, input_str):
        raise InputValidationException("Invalid format or range.")


class Period:
    def __init__(self, period_s: str, period_id: int):
        self.hundreds = int(period_s[-3]) if len(period_s) >= 3 else 0
        self.tens_and_ones = int(period_s[-2::])
        self.period_id = period_id

    def is_zero(self):
        return self.hundreds == 0 and self.tens_and_ones == 0


def ceil_div(a, b):
    return -(a // -b)


def _parse_periods(number_str: str) -> []:
    periods, s_parse_start, s_parse_end = [], max(len(number_str) - 3, 0), len(number_str)
    for period_id in range(ceil_div(len(number_str), 3)):
        periods.append(Period(number_str[s_parse_start:s_parse_end], period_id))
        s_parse_start, s_parse_end = max(s_parse_start - 3, 0), s_parse_start

    return [p for p in periods[::-1] if not p.is_zero()]


def _translate_period_numbers(period: Period) -> str:
    word = []
    if period.hundreds != 0:
        word.append(f'{ONES_MAP[period.hundreds]} hundred')

    if period.tens_and_ones != 0:
        word.append(TENS_AND_ONES_MAP[period.tens_and_ones])

    return ' and '.join(word)


def _translate_a_period(period: Period) -> str:
    period_numbers = _translate_period_numbers(period=period)
    return f'{period_numbers} {PERIOD_MAP[period.period_id]}' if period.period_id != 0 else f'{period_numbers}'


def _get_period_separation_character(period: Period):
    return ',' if period.hundreds != 0 and period.tens_and_ones != 0 else ' and'


def _translate_periods(periods: []) -> str:
    translated_per_s = _translate_a_period(periods[0])
    for i in range(1, len(periods)):
        translated_per_s += f'{_get_period_separation_character(periods[i])} {_translate_a_period(periods[i])}'

    return translated_per_s


def spell(number_str: str):
    _validate_input(input_str=number_str)
    if number_str == ZERO_DIGIT_S:
        return ONES_MAP[0]
    periods = _parse_periods(number_str=number_str)
    return _translate_periods(periods=periods)
