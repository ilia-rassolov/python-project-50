from gendiff.make_diff import generate_diff
from gendiff.make_diff import generate_diff_node
from gendiff.parser_file import parsing_file
from gendiff.dict_val_formatter import to_str_value, to_str
from collections import defaultdict


def stylish(filepath1_, filepath2_):
    data1_: dict = parsing_file(filepath1_)
    data2_: dict = parsing_file(filepath2_)

    data1 = to_str_value(data1_)
    data2 = to_str_value(data2_)
    print('data1 = ', data1)
    print('data2 = ', data2)

    # объединим ключи через множество в список
    keys_data = list(set(data1 | data2))
    keys_data.sort()
    print('keys_data = ', keys_data)
    result = ''
    # print(f"{string=}")

    def inner(node1, node2, keys_inner=keys_data, level=1):
        # string = f"{'    ' * (level - 1)}"
        string = '{\n'
        for key in keys_inner:
            print('key =', key)
            print(f"{node1=}", f"{node2=}")
            (value1, symbol1), (value2, symbol2) = generate_diff_node(key, node1, node2)
            print(f"{generate_diff_node(key, node1, node2)=}")
            keys_children = []
            for val, symbol in ((value1, symbol1), (value2, symbol2)):
                # print(f"{value1=}", f"{symbol1=}", f"{value2=}", f"{symbol2=}")
                if not isinstance(val, dict):
                    string += f"{'    ' * (level - 1)}{symbol}{key}: {to_str(val)}\n"
                    print(f"{string=}")
                elif isinstance(val, dict) and val:
                    children = val
                    # объединим ключи через множество в список
                    keys_children.extend(list(children.keys()))
                    keys_children = list(set(keys_children))
                    keys_children.sort()
                    print(f"{keys_children=}")
            if keys_children:
                level += 1
                print(f"{level=}")
                # result += string
                inner(value1, value2, keys_children, level)
            string += '}\n'
    print(f"{result=}")
    inner(data1, data2)
    # result = str.join(string)
    return result

print(f"{stylish('json_files/file1_stilish.json', 'json_files/file2_stilish.json')=}")

# if key in node1:
#                 if key in node2:
#                     value1, value2, acc = generate_diff_node(node1, node2, key, level)
#                     print('value1 = ', value1, type(value1), type(value2))
#                     if not isinstance(value1, dict) and not isinstance(value2, dict):
#                         print('value1 = ', value1, 'value2 = ', value2, 'acc = ', acc)
#                         if value1 == value2:
#                             string.append(f"{'    ' * (acc - 1)}{'    '}{key}: {value1}\n")
#                         else:
#                             string.append(f"{'    ' * (acc - 1)}{'  - '}{key}: {value1}\n")
#                             string.append(f"{'    ' * (acc - 1)}{'  + '}{key}: {value2}\n")
#                     else:
#                         children1, children2 = value1, value2
#                         print('children1 = ', children1, 'children2 = ', children2)
#                         keys_children = list(set(children1 | children2))
#                         keys_children.sort()
#                         print('keys_children = ', keys_children, acc)
#                         inner(children1, children2, keys_children, acc)
#                 else:
#                     string.append(f"{'  - ' * level}{key}: {node1[key]}\n")
#             # elif not isinstance(node2[key], dict):
#             #     string.append(f"{'    ' * (level - 1)}{'  + '}{key}: {node2[key]}\n")
#             else:
#                 string.append(f"{'    ' * (level - 1)}{'  + '}{key}: {node2[key]}\n")
#             string.append(f"{'    ' * level}")
#         string.append('}\n')
#     inner(data1, data2)
#     result = str.join(string)
#     print(result)
    # diff = generate_diff('fixtures/file1_stylish.json', 'fixtures/file2_stylish.json')
    # assert diff == result
    # pass

# data1_str = {'host': 'hexlet.io', 'timeout': '50', 'proxy': '123.234.53.22', 'follow': 'false'}
# data2_str = {'timeout': '20', 'verbose': 'true', 'host': 'hexlet.io'}
# print(generate_diff_key('proxy'))
# print(test_generate_diff())