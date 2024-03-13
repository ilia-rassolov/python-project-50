from gendiff.parser_file import parsing_file
from gendiff.dict_val_formatter import to_str_value


def generate_diff(filepath1_, filepath2_):
    data1: dict = parsing_file(filepath1_)
    data2: dict = parsing_file(filepath2_)
    data1_ = to_str_value(data1)
    data2_ = to_str_value(data2)
    print(data1_, data2_)

    # объединим ключи через множество в список
    keys = list(set(data1_ | data2_))
    keys.sort()

    # запишем различия между данными в строку
    result = '{\n'
    for key in keys:
        if key in data1_:
            if key in data2_:
                if data1_[key] == data2_[key]:
                    result += f'    {key}: {data1_[key]}\n'
                else:
                    result += f'  - {key}: {data1_[key]}\n'
                    result += f'  + {key}: {data2_[key]}\n'
            else:
                result += f'  - {key}: {data1_[key]}\n'
        else:
            result += f'  + {key}: {data2_[key]}\n'
    result += '}'
    return result
#
# print(generate_diff('yaml_files/file1_stilish.json', 'yaml_files/file2_stilish.json'))

from collections import defaultdict

def generate_diff_node(data1_, data2_, node, level=1):

    if not isinstance(data1_, dict) and not isinstance(data2_, dict):
        return data1_, data2_, level
    value_1 = data1_[node]
    value_2 = data2_[node]
    level += 1
    children_1 = value_1
    children_2 = value_2
    return children_1, children_2, level

data1 = {'a': 1, 'b': 2}
data2 = {'c': 3, 'a': 1}
data3 = ''
data4 = defaultdict()
data1.setdefault('key', []).append(data3)
print(data1)



# data1 =  {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}
data1 = 'aaa'
data2 =  {'common': {'follow': False, 'setting1': 'Value 1', 'setting3': None, 'setting4': 'blah blah', 'setting5': {'key5': 'value5'}, 'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}}, 'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'}, 'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
# print(generate_diff_node(data1, data4, 'b'))



# from gendiff.parser_file import parsing_file
#
#
# def generate_diff(filepath1_, filepath2_):
#     data1_: dict = parsing_file(filepath1_)
#     data2_: dict = parsing_file(filepath2_)
#
#     # объединим ключи через множество в список
#     keys = list(set(data1_ | data2_))
#     # print('keys = ', keys)
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
#     data1_str = to_str_value(data1_)
#     data2_str = to_str_value(data2_)
#
#     # эта функция описывает внутреннее представление -
#     # делает diff по каждому ключу
#
#
#     # запишем различия между данными в строку
#     result = '{\n'
#     for key in keys:
#         if key in data1_str:
#             if key in data2_str:
#                 generate_diff_node(key) = (value_1, value_2)
#                 level = 1
#                 if value_1 == value_2:
#                     result += f'{' '*level}{key}: {data1_str[key]}\n'
#                 else:
#                     result += (f'  - {key}: {data1_str[key]}\n  + '
#                                f'{key}: {data2_str[key]}\n')
#             else:
#                 result += f'  - {key}: {data1_str[key]}\n'
#         else:
#             result += f'  + {key}: {data2_str[key]}\n'
#     result += '}'
#
#     return result
#
#
#
#
#
# data1_str = {'host': 'hexlet.io', 'timeout': '50', 'proxy': '123.234.53.22', 'follow': 'false'}
# data2_str = {'timeout': '20', 'verbose': 'true', 'host': 'hexlet.io'}
# print(generate_diff('json_files/file1_stilish.json', 'json_files/file2_stilish.json'))
# print(generate_diff_key('proxy'))