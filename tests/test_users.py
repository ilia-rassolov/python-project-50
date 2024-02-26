from gendiff.make_diff import generate_diff
from gendiff.parser_file import parsing_file
import pytest


# @pytest.mark.parametrize("filepath1", ['tests/fixtures/f_1input.json',
#                                        'tests/fixtures/f_1input.yaml',
#                                        'tests/fixtures/file.yml'])
# @pytest.mark.parametrize("filepath2", ['tests/fixtures/f_2input.json',
#                                        'tests/fixtures/f_2input.yaml'])
# def test_generate_diff(filepath1, filepath2):
#
#     data1 = parsing_file(filepath1)
#     data2 = parsing_file(filepath2)
#     ...
#     ...
#     diff = generate_diff("filepath1", "filepath2")
#     assert diff == result
#     pass

def test_generate_diff():
    data1 = parsing_file('tests/fixtures/f1_input.yaml')
    data2 = parsing_file('tests/fixtures/f2_input.yaml')

    # объединим ключи через множество в список
    keys = list(set(list(data1.keys())
                    + list(data2.keys())))
    keys.sort()

    # эта функция форматирует значения словарей в строки
    def to_str_value(data):
        data_str = {}
        for key in data.keys():
            if isinstance(data[key], bool):
                data_str[key] = str(data[key]).lower()
            elif data[key] == 'null':
                data_str[key] = None
            else:
                data_str[key] = str(data[key])
        return data_str

    data1_str = to_str_value(data1)
    data2_str = to_str_value(data2)

    # запишем различия между данными в file_out и прочтём их
    string = open('tests/fixtures/file_out', 'w')
    string.write('{\n')
    for key in keys:
        # print(key)
        if key in data1_str:
            if key in data2_str:
                if data1_str[key] == data2_str[key]:
                    string.write(f'    {key}: {data1_str[key]}\n')
                else:
                    string.write(f'  - {key}: {data1_str[key]}\n  + {key}: {data2_str[key]}\n')
            else:
                string.write(f'  - {key}: {data1_str[key]}\n')
        else:
            string.write(f'  + {key}: {data2_str[key]}\n')
    string.write('}')
    string = open('tests/fixtures/file_out')
    result = string.read()

    diff = generate_diff('tests/fixtures/f1_input.yaml', 'tests/fixtures/f2_input.yaml')
    assert diff == result
