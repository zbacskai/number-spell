import argparse
import re
import sys
from os.path import dirname as d
from os.path import abspath

root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)

INPUT_REGEX = re.compile(r"^0$|^[1-9][0-9]{0,4}$|^10{5}$")


class ValidateInputNumber(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        if not re.match(INPUT_REGEX, values):
            parser.error(f"Please enter an integer number between 0 and 100000. Got: {values}")

        setattr(namespace, self.dest, values)


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("number", action=ValidateInputNumber, type=str, help="An integer number between 0 and 100000")