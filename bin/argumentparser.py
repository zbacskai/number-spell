"""

 Entry point for command line interface of number-to-word command.

 This command spells numbers given in digits in British English.

 Currently numbers in the range of 0..100000 supported. (0 and 100000 inclusive)

 2023 September - Zoltan Bacskai - z.bacskai.jr@gmail.com

"""
import argparse
import re
import sys
from os.path import dirname as d
from os.path import abspath

root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)

INPUT_REGEX = re.compile(r"^0$|^[1-9][0-9]{0,4}$|^10{5}$")

RANGE_DEF = "integer number between 0 and 100000"


class ValidateInputNumber(argparse.Action):
    """
    Validator required by argparse. Input validation is also implemented in spell function, but I found it
    more elegant to report invalid input using argpareser's own method.
    """
    def __call__(self, parser, namespace, values, option_string=None):
        if not re.match(INPUT_REGEX, values):
            parser.error(f"Please enter an {RANGE_DEF}. Got: {values}")

        setattr(namespace, self.dest, values)


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("number", action=ValidateInputNumber, type=str, help=f"An {RANGE_DEF}")
