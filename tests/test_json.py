from gendiff.formatters.json_ import json_
from gendiff.parser_file import parsing_file
import pytest


@pytest.mark.parametrize("filepath1, filepath2, expected", [
                        ('tests/fixtures/nest_f1.json', 'tests/fixtures/nest_f2.json', 'tests/fixtures/exp_json'),
                        ('tests/fixtures/nest_f1.yaml', 'tests/fixtures/nest_f2.yaml', 'tests/fixtures/exp_json'),])
def test_json(filepath1, filepath2, expected):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)

    string = open(expected)
    result_json = string.read()

    diff = json_(data1, data2)
    assert diff == result_json
    pass
