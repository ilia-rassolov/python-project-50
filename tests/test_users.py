# from gendiff.make_diff import generate_diff
# from gendiff.parser_file import parsing_file
# import pytest
#
#
# @pytest.mark.parametrize("filepath1", ['tests/fixtures/f1_input.json',
#                                        'tests/fixtures/f1_input.yaml',
#                                        'tests/fixtures/file.yml'])
# @pytest.mark.parametrize("filepath2", ['tests/fixtures/f2_input.json',
#                                        'tests/fixtures/f2_input.yaml'])
# def test_generate_diff(filepath1, filepath2):
#
#     data1: dict = parsing_file(filepath1)
#     data2: dict = parsing_file(filepath2)
#
#     # объединим ключи через множество в список
#     keys = list(set(data1 | data2))
#     keys.sort()
#
#     # эта функция форматирует значения словарей в строки
#     def to_str_value(data: dict):
#         data_str = {}
#         for key in data:
#             if isinstance(data[key], bool):
#                 data_str[key] = str(data[key]).lower()
#             elif data[key] == 'null':
#                 data_str[key] = None
#             else:
#                 data_str[key] = str(data[key])
#         return data_str
#
#     data1_str = to_str_value(data1)
#     data2_str = to_str_value(data2)
#
#     # запишем различия между данными в file_out и прочтём их
#     string = open('tests/fixtures/file_out', 'w')
#     string.write('{\n')
#     for key in keys:
#         # print(key)
#         if key in data1_str:
#             if key in data2_str:
#                 if data1_str[key] == data2_str[key]:
#                     string.write(f'    {key}: {data1_str[key]}\n')
#                 else:
#                     string.write(f'  - {key}: {data1_str[key]}\n  + {key}: {data2_str[key]}\n')
#             else:
#                 string.write(f'  - {key}: {data1_str[key]}\n')
#         else:
#             string.write(f'  + {key}: {data2_str[key]}\n')
#     string.write('}')
#     string = open('tests/fixtures/file_out')
#     result = string.read()
#
#     diff = generate_diff(filepath1, filepath2)
#     assert diff == result
#     pass

from gendiff.make_diff import generate_diff
from gendiff.make_diff import generate_diff_node
from gendiff.parser_file import parsing_file

# import pytest
#
#
# @pytest.mark.parametrize("filepath1", ['tests/fixtures/f1_input.json',
#                                        'tests/fixtures/f1_input.yaml',
#                                        'tests/fixtures/file.yml'])
# @pytest.mark.parametrize("filepath2", ['tests/fixtures/f2_input.json',
#                                        'tests/fixtures/f2_input.yaml'])
def test_generate_diff():

    data1: dict = parsing_file('fixtures/file1.json')
    data2: dict = parsing_file('fixtures/file2.json')
    print('data1 = ', data1)
    print('data2 = ', data2)

    # объединим ключи через множество в список
    keys_data = list(set(data1 | data2))
    keys_data.sort()
    print('keys_data = ', keys_data)

    # запишем различия между данными в file_out и прочтём их
    string = open('fixtures/file_out', 'w')
    string.write('{\n')
    def inner(node1, node2, keys_inner=keys_data, level=1):
        for key in keys_inner:
            print('key =', key)
            if key in node1:
                if key in node2:
                    string.write(f"{' ' * (level * 4 - 2)}{key}")
                    string.write(': {\n')
                    value1, value2, acc = generate_diff_node(node1, node2, key, level)
                    print('value1 = ', value1, type(value1), type(value2))
                    if not isinstance(value1, dict) and not isinstance(value2, dict):
                        print('value1 = ', value1, 'value2 = ', value2, 'acc = ', acc)
                        if value1 == value2:
                            string.write(f"{' ' * (acc * 4 - 2)}{key}: {value1}\n")
                        else:
                            string.write(f"{'  - ' * acc}{key}: {value1}\n")
                            string.write(f"{'  + ' * acc}{key}: {value2}\n")
                    else:
                        children1, children2 = value1, value2
                        print('children1 = ', children1, 'children2 = ', children2)
                        keys_children = list(set(children1 | children2))
                        keys_children.sort()
                        print('keys_children = ', keys_children, acc)
                        inner(children1, children2, keys_children, acc)
                else:
                    string.write(f"{'  - ' * level}{key}: {node1[key]}\n")
            else:
                string.write(f"{'    ' * (level - 1)}{'  + '}{key}: {node2[key]}\n")
            string.write(f"{'    ' * level}")
        string.write('}\n')
    inner(data1, data2)
    string = open('fixtures/file_out')
    result = string.read()
    print(result)
    # diff = generate_diff('fixtures/file1.json', 'fixtures/file2.json')
    # assert diff == result
    # pass

# data1_str = {'host': 'hexlet.io', 'timeout': '50', 'proxy': '123.234.53.22', 'follow': 'false'}
# data2_str = {'timeout': '20', 'verbose': 'true', 'host': 'hexlet.io'}
# print(generate_diff_key('proxy'))
print(test_generate_diff())