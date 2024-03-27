from gendiff.make_diff import generate_diff
from gendiff.parser_file import parsing_file
import pytest


@pytest.mark.parametrize("filepath1", ['tests/fixtures/f1_input.json',
                                       'tests/fixtures/f1_input.yaml',
                                       'tests/fixtures/file.yml'])
@pytest.mark.parametrize("filepath2", ['tests/fixtures/f2_input.json',
                                       'tests/fixtures/f2_input.yaml'])
def test_generate_diff(filepath1, filepath2):

    data1: dict = parsing_file(filepath1)
    data2: dict = parsing_file(filepath2)

    # объединим ключи через множество в список
    keys = list(set(data1 | data2))
    keys.sort()

    # эта функция форматирует значения словарей в строки
    def to_str_value(data: dict):
        data_str = {}
        for key in data:
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

    diff = generate_diff(filepath1, filepath2)
    assert diff == result
    pass

# def test_generate_diff():
#
#     data1_: dict = parsing_file('fixtures/file1.json')
#     data2_: dict = parsing_file('fixtures/file2.json')
#     data1 = to_str_value(data1_)
#     data2 = to_str_value(data2_)
#
#     print('data1 = ', data1)
#     print('data2 = ', data2)
#
#     # объединим ключи через множество в список
#     keys_data = list(set(data1 | data2))
#     keys_data.sort()
#     print('keys_data = ', keys_data)
#
#     # запишем различия между данными в file_out и прочтём их
#     string = open('fixtures/file_out', 'w')
#     def inner(node1, node2, keys_inner=keys_data, level=0):
#         string.write(' ' * level)
#         string.write('{\n')
#         for key in keys_inner:
#             print('key =', key)
#             print(f"{node1=}", f"{node2=}")
#             (value1, symbol1), (value2, symbol2) = generate_diff_node(key, node1, node2)
#             print(f"{generate_diff_node(key, node1, node2)=}")
#             keys_children = []
#             for val, symbol in ((value1, symbol1), (value2, symbol2)):
#                 print(f"{value1=}", f"{symbol1=}", f"{value2=}", f"{symbol2=}")
#                 if not isinstance(val, dict):
#                     string.write(f"{'    ' * (level)}{symbol}{key}: {to_str(val)}\n")
#                     print(f"{string=}")
#                 elif isinstance(val, dict) and val:
#                     string.write(f"{'    ' * level}{symbol}{key}:")
#                     children = val
#                     # объединим ключи через множество в список
#                     keys_children.extend(list(children.keys()))
#                     keys_children = list(set(keys_children))
#                     keys_children.sort()
#                     print(f"{keys_children=}")
#             if keys_children:
#                 level += 1
#                 print(f"{level=}")
#                 inner(value1, value2, keys_children, level)
#         string.write(' ' * level)
#         string.write('}\n')
#     inner(data1, data2)
#     string = open('fixtures/file_out')
#     result = string.read()
#     return result
#
# print(test_generate_diff())