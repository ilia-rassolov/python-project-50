from gendiff.formatters.plain import plain
from gendiff.parser_file import parsing_file
import pytest


@pytest.mark.parametrize("tests/filepath1, filepath2, expected", [
                        ('tests/fixtures/nest_f1.json', 'tests/fixtures/nest_f2.json', 'fixtures/exp_plain'),
                        ('tests/fixtures/nest_f1.yaml', 'tests/fixtures/nest_f2.yaml', 'fixtures/exp_plain'),])
def test_plain(filepath1, filepath2, expected):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)

    string = open(expected)
    expected_result = string.read()

    diff = plain(data1, data2)
    assert diff == expected_result
    pass