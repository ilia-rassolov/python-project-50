from gendiff.formatters.plain import plain
from gendiff.parser_file import parsing_file
import pytest


@pytest.mark.parametrize("filepath1, filepath2, expected", [
                        ('tests/fixtures/nest_f1.json', 'tests/fixtures/nest_f2.json', 'tests/fixtures/exp_plain'),
                        ('tests/fixtures/nest_f1.yaml', 'tests/fixtures/nest_f2.yaml', 'tests/fixtures/exp_plain'),])
def test_plain(filepath1, filepath2, expected):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)

    string = open(expected)
    result_plain = string.read()

    diff = plain(data1, data2)
    assert diff == result_plain
    pass
