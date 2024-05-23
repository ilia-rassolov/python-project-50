from gendiff.make_diff import generate_diff
import pytest


@pytest.mark.parametrize("filepath1, filepath2, formatter", [
    ('tests/fixtures/nest_f1.json', 'tests/fixtures/nest_f2.json', 'stylish'),
    ('tests/fixtures/nest_f1.yaml', 'tests/fixtures/nest_f2.yaml', 'stylish'),
    ('tests/fixtures/nest_f1.json', 'tests/fixtures/nest_f2.json', 'plain'),
    ('tests/fixtures/nest_f1.yml', 'tests/fixtures/nest_f2.json', 'plain'),
    ('tests/fixtures/nest_f1.yml', 'tests/fixtures/nest_f2.yaml', 'json'),
    ('tests/fixtures/nest_f1.yaml', 'tests/fixtures/nest_f2.yaml', 'json')])
def test_generate_diff(filepath1, filepath2, formatter):

    fixture = f'tests/fixtures/exp_{formatter}'
    string = open(fixture)
    expected_result = string.read()
    diff = generate_diff(filepath1, filepath2, formatter)
    assert diff == expected_result
