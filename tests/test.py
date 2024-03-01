import os
import json
import pytest
from deepdiff import DeepDiff

from Metrics.MetricsClusterHandler import MetricsClusterHandler
from identity.IdentityClusterHandler import IdentityClusterHandler


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
    load_test_cases('identities_test_cases'),
    ids=lambda test_case: test_case['test_name']
)
def test_identities(test_case):
    test_input = test_case['input']
    expected_output = test_case['expected']
    cluster_handler = IdentityClusterHandler()
    actual_output = cluster_handler.handle_items(test_input)
    diff = DeepDiff(actual_output, expected_output, ignore_order=True)
    assert not diff, f'Difference found: {diff}'


@pytest.mark.parametrize(
    "test_case",
    load_test_cases('metrics_test_cases'),
    ids=lambda test_case: test_case['test_name']
)
def test_metrics(test_case):
    test_input = test_case['input']
    expected_output = test_case['expected']
    cluster_handler = MetricsClusterHandler()
    actual_output = cluster_handler.handle_items(test_input)
    diff = DeepDiff(actual_output, expected_output, ignore_order=True)
    assert not diff, f'Difference found: {diff}'
