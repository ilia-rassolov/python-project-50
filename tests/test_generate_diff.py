from gendiff.make_diff import generate_diff
from gendiff.parser_file import parsing_file
from gendiff.formatters.make_str import to_str
import pytest


@pytest.mark.parametrize("filepath1, filepath2, formatter", [
       ('tests/fixtures/flat_f1.json', 'tests/fixtures/flat_f2.json', 'flat'),
       ('tests/fixtures/flat_f1.yaml', 'tests/fixtures/flat_f2.yaml', 'flat'),
       ('tests/fixtures/flat_f1.json', 'tests/fixtures/flat_f2.yaml', 'flat'),
       ('tests/fixtures/flat_f1.yml', 'tests/fixtures/flat_f2.json', 'flat'),
       ('tests/fixtures/nest_f1.json', 'tests/fixtures/nest_f2.json', 'stylish'),
       ('tests/fixtures/nest_f1.yaml', 'tests/fixtures/nest_f2.yaml', 'stylish'),
       ('tests/fixtures/nest_f1.json', 'tests/fixtures/nest_f2.json', 'plain'),
       ('tests/fixtures/nest_f1.yaml', 'tests/fixtures/nest_f2.yaml', 'json')])
def test_generate_diff(filepath1, filepath2, formatter):

    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)

    if formatter == 'flat':

        # объединим ключи
        keys = list(set(data1 | data2))
        keys.sort()

        # запишем различия между данными в exp_flat и прочтём их
        string = open('tests/fixtures/exp_flat', 'w')
        string.write('{\n')
        for key in keys:
            # print(key)
            if key in data1:
                if key in data2:
                    if data1[key] == data2[key]:
                        string.write(f'    {key}: {to_str(data1[key])}\n')
                    else:
                        string.write(f'  - {key}: {to_str(data1[key])}\n  + {key}: {to_str(data2[key])}\n')
                else:
                    string.write(f'  - {key}: {to_str(data1[key])}\n')
            else:
                string.write(f'  + {key}: {to_str(data2[key])}\n')
        string.write('}')
        fixture = 'tests/fixtures/exp_flat'
        string = open(fixture)
        expected_result = string.read()
        diff = generate_diff(filepath1, filepath2, formatter)
        assert diff == expected_result
        pass
    elif formatter in ('stylish', 'plain', 'json'):
        fixture = f'tests/fixtures/exp_{formatter}'
        string = open(fixture)
        expected_result = string.read()
        diff = generate_diff(filepath1, filepath2, formatter)
        assert diff == expected_result
        pass
    else:
        raise ValueError(f"Unsupported file format: {formatter}")
