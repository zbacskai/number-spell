"""
 The constants used to do the translation of digits to words in British English

 2022 September - Zoltan Bacskai - z.bacskai.jr@gmail.com
"""
ONES_MAP = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Helper structures to translate twodigit numbers
_REGULAR_TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
_TENS_AND_ONES_REGULAR_MAP = [
    f'{_REGULAR_TENS[i // 10]}-{ONES_MAP[i % 10]}' if i % 10 != 0 else f'{_REGULAR_TENS[i // 10]}' for i in
    range(0, 80)]

# We construct a mapping of english words for all numbers from 0 to 99
TENS_AND_ONES_MAP = ONES_MAP + [
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'] + _TENS_AND_ONES_REGULAR_MAP

# A structure to efficiently map period names.
PERIOD_MAP = ['one', 'thousand', 'million']
