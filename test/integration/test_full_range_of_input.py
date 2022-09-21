from number_spell.spell import spell
import json
import os

TEST_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def test_full_range_input():
    with open(os.path.join(TEST_DIR_PATH, 'expected-results.json'), 'r') as er:
        expected_result = json.load(er)
        for i in range(0, 100000 + 1):
            assert expected_result[f'{i}'] == spell(f'{i}')
