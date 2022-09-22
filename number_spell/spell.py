"""

 Main implementation of the translator and parsers

 2022 September - Zoltan Bacskai - z.bacskai.jr@gmail.com

"""
from number_spell.constants import ONES_MAP, TENS_AND_ONES_MAP, PERIOD_MAP
from typing import List
import re

# The regular expression to check that input is in the range of 0 an 100000 (0 and 100000 inclusive)
INPUT_REGEX = re.compile(r"^0$|^[1-9][0-9]{0,4}$|^10{5}$")

ZERO_DIGIT_S = '0'


# Exception thrown if input validation failed
class InputValidationException(Exception):
    pass


def _validate_input(input_str: str) -> None:
    if not re.match(INPUT_REGEX, input_str):
        raise InputValidationException("Invalid format or range.")


class Period:
    """
    A period is a 3 or fewer digits representing ones, thousands, millions in a number
    """
    def __init__(self, period_s: str, period_id: int) -> None:
        """

        :param period_s: a string representing the period. 1-3 digits
        :param period_id: a number to look up the period name.
                          0 == ones, 1 == 1000^1 == thousands, 2 == 1000^2 == millions
        """
        self.hundreds = int(period_s[-3]) if len(period_s) >= 3 else 0
        self.tens_and_ones = int(period_s[-2::])
        self.period_id = period_id

    def is_zero(self) -> bool:
        """
        Function to check if the period only contains 0 digits
        :return: true if period only contains 0 digits
        """
        return self.hundreds == 0 and self.tens_and_ones == 0


def ceil_div(a: int, b: int) -> int:
    return -(a // -b)


def _parse_periods(number_str: str) -> List[Period]:
    """
    Function to parse a string  representing a number to a list of periods
    :param number_str: The string representing the number
    :return: a list of period objects. The list read from left (the lowest index) to right (the highest index) shall
             contain the periods of the given input number.
    """
    periods, s_parse_start, s_parse_end = [], max(len(number_str) - 3, 0), len(number_str)
    for period_id in range(ceil_div(len(number_str), 3)):
        periods.append(Period(number_str[s_parse_start:s_parse_end], period_id))
        s_parse_start, s_parse_end = max(s_parse_start - 3, 0), s_parse_start

    return [p for p in periods[::-1] if not p.is_zero()]


def _translate_period_numbers(period: Period) -> str:
    """
    Function to convert the number in the period. It follows spelling rules. Pronounce hundreds first and then if there
    are any tens and ones connect them with an 'and' word.

    :param period: The period object containing a 3 or fewer digit number.
    :return: The British English spelling/pronunciation of the input number stored in the period.
    """
    word = []
    if period.hundreds != 0:
        word.append(f'{ONES_MAP[period.hundreds]} hundred')

    if period.tens_and_ones != 0:
        word.append(TENS_AND_ONES_MAP[period.tens_and_ones])

    return ' and '.join(word)


def _translate_a_period(period: Period) -> str:
    """
    This function does the whole translation of a period. First we pronounce the numbers on the period then we say the
    name of the period. (thousand or million, etc...)

    :param period: The period object containing 3 or fewer digits
    :return: The British English pronunciation of the period. Including the number and the name of the period
    """
    period_numbers = _translate_period_numbers(period=period)
    return f'{period_numbers} {PERIOD_MAP[period.period_id]}' if period.period_id != 0 else f'{period_numbers}'


def _get_period_separation_character(period: Period) -> str:
    """
    Periods are separated by , or and word depending on whether there are any hundreds and tens and ones in the next
    period. For example:
        1001 - one thousand and one (as there are only ones)
        1101 - one thousand, one hundred and one (as both hundreds and tens and ones are present in the period)

    :param period: The period object
    :return: ',' or ' and'
    """
    return ',' if period.hundreds != 0 and period.tens_and_ones != 0 else ' and'


def _translate_periods(periods: List[Period]) -> str:
    """
    Function translate the list of periods to a hunan readable British English pronunciation.
    :param periods: A list of periods representing a number
    :return: The British English pronunciation of the number represented by the periods.
    """
    translated_per_s = _translate_a_period(periods[0])
    for i in range(1, len(periods)):
        translated_per_s += f'{_get_period_separation_character(periods[i])} {_translate_a_period(periods[i])}'

    return translated_per_s


def spell(number_str: str) -> str:
    """
    The main function to do the translation from a string representation of a number to British English
    word representation.

    :param number_str: The string containing the number to be translated.
    :return: The British English translation/pronunciation of the number.
    """
    _validate_input(input_str=number_str)
    if number_str == ZERO_DIGIT_S:
        return ONES_MAP[0]
    periods = _parse_periods(number_str=number_str)
    return _translate_periods(periods=periods)
