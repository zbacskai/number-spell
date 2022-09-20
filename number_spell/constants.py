ONES_MAP = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

_REGULAR_TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
_TENS_AND_ONES_REGULAR_MAP = [
    f'{_REGULAR_TENS[i // 10]}-{ONES_MAP[i % 10]}' if i % 10 != 0 else f'{_REGULAR_TENS[i // 10]}' for i in
    range(0, 80)]

TENS_AND_ONES_MAP = ONES_MAP + [
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'] + _TENS_AND_ONES_REGULAR_MAP

PERIOD_MAP = ['', 'thousand', 'million']
