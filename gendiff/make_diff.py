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

def generate_diff_node(key_, node1_, node2_):
    if key_ in node1_:
        if key_ in node2_:
            value_1 = node1_[key_]
            value_2 = node2_[key_]
            # if not isinstance(value_1, dict) and not isinstance(value_2, dict):
            if value_1 == value_2:
                return (value_1, '    '), ({}, None)
            else:
                return (value_1, '  - '), (value_2, '  + ')
            # elif not isinstance(value_1, dict) and isinstance(value_2, dict):
            #     return '  - ', value_1, '  + ', value_2
        else:
            return (node1_[key_], '  - '), ({}, None)
    else:
        return ({}, None), (node2_[key_], '  + ')




# data1 = {'a': 1, 'b': 2}
# data2 = {'c': 3, 'a': 1}
# print(f"{generate_diff_node(data1, data2, 'b')}")
# data3 = ''
# data4 = defaultdict(dict)
# data1.setdefault('key', []).append(data3)
# data4['11']
# # print(data4)
# data4 = defaultdict(dict)
# print(f"{data4=}")


# data1 =  {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}
# data1 = 'aaa'
# data2 =  {'common': {'follow': False, 'setting1': 'Value 1', 'setting3': None, 'setting4': 'blah blah', 'setting5': {'key5': 'value5'}, 'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}}, 'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'}, 'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
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



def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)