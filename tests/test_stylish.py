from gendiff.formatters.stylish import stylish
from gendiff.parser_file import parsing_file
import pytest


@pytest.mark.parametrize("filepath1, filepath2, expected", [
                        ('tests/fixtures/nest_f1.json', 'tests/fixtures/nest_f2.json', 'tests/fixtures/exp_json.txt'),
                        ('tests/fixtures/nest_f1.yaml', 'tests/fixtures/nest_f2.yaml', 'tests/fixtures/exp_yaml.txt'),])
def test_stylish(filepath1, filepath2, expected):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)

    string = open(expected)
    expected_result = string.read()

    diff = stylish(data1, data2)
    assert diff == expected_result
    pass
