from gendiff.formatters.stylish import stylish
import pytest



@pytest.mark.parametrize("filepath1, filepath2, expected", [
                         ('fixtures/nest_f1.json', 'fixtures/nest_f2.json', 'fixtures/exp_json.txt'),
                         ('fixtures/nest_f1.yaml', 'fixtures/nest_f2.yaml', 'fixtures/exp_yaml.txt'),
])

def test_stylish(filepath1, filepath2, expected):
    with open(expected) as file:
        expected_result = file.read()

    diff = stylish(filepath1, filepath2)
    assert diff == expected_result
    pass
