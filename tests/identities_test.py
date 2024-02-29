import os
import json
import pytest
from deepdiff import DeepDiff

from identities import identities_handler


def load_test_cases(directory):
    test_cases = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as file:
                test_case_data = json.load(file)
                test_case_data['test_name'] = filename[:-5]
                test_cases.append(test_case_data)
    return test_cases


@pytest.mark.parametrize(
    "test_case",
    load_test_cases('test_cases'),
    ids=lambda test_case: test_case['test_name']
)
def test_run_test_cases(test_case):
    test_input = test_case['input']
    expected_output = test_case['expected']
    actual_output = identities_handler(test_input)
    diff = DeepDiff(actual_output, expected_output, ignore_order=True)
    assert not diff, f'Difference found: {diff}'


