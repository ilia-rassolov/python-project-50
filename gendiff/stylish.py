from gendiff.parser_file import parsing_file
from gendiff.dict_val_formatter import to_str
import itertools

# эта функция создаёт внутреннее представление - промежуточную структуру данных tree_differences,
# где указаны различия между data1 и data2 по параметрам: ключ, тип изменения, значения по ключу


def build_tree(data_input, data_out):

    # эта функция формирует потомков из 2-х словарей по всем ключам

    def inner(data1, data2):
        children_tree = []
        keys = list(set(data1 | data2))
        keys.sort()

        # эта функция формирует потомков из словарей по указанному ключу,
        # но только в том случае, если эти потомки оба не словари

        def build_children(dict1_, dict2_, key_):
            children_ = []
            for dict_ in (dict1_, dict2_):
                if key_ in dict_:
                    if isinstance(dict_[key_], dict):
                        value_ = inner(dict_[key_], dict_[key_])
                    else:
                        value_ = [to_str(dict_[key_])]
                    children_.extend(value_)
            return children_

        for key in keys:
            # print(f"{key=}")
            current_dict = {}
            current_dict['key'] = key
            value1 = data1.get(key, 'absent')
            value2 = data2.get(key, 'absent')

            if isinstance(value1, dict) and isinstance(value2, dict):
                current_dict['children'] = inner(value1, value2)
                if value1 == value2:
                    current_dict['type'] = 'unchanged'
                else:
                    current_dict['type'] = 'nested'
            else:
                current_dict['children'] = build_children(data1, data2, key)
                if value1 == value2:
                    current_dict['type'] = 'unchanged'
                    # в этой строке устраним дублирование значений
                    current_dict['children'] = list(set(current_dict['children']))
                elif value1 == 'absent':
                    current_dict['type'] = 'added'
                elif value2 == 'absent':
                    current_dict['type'] = 'deleted'
                else:
                    current_dict['type'] = 'changed'

            children_tree.append(current_dict)
        return children_tree
    return {'type': 'root', 'children': inner(data_input, data_out)}


def stylish(filepath1_, filepath2_):
    data1 = parsing_file(filepath1_)
    data2 = parsing_file(filepath2_)
    # print('data1 = ', data1)
    # print('data2 = ', data2)
    tree_differences = build_tree(data1, data2)
    # print(f"{tree_differences=}")

    def build_string(tree, depth=0):
        # print(f"{tree=}")
        nods = tree['children']
        string = ''

        def iter_(node, depth_=0):
            # print(f"{node=}")
            if not isinstance(node, dict):
                return node
            indent = ' ' * 4 * depth_
            line = []
            if node['type'] == 'nested':
                line.append(f"{indent}    {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'unchanged':
                line.append(f"{indent}    {node['key']}: ")
                line.append(f"{iter_(node['children'][0], depth_ + 1)}")
            elif node['type'] == 'changed':
                line.append(f"{indent}  - {node['key']}: ")
                line.append(f"{iter_(node['children'][0])}\n")
                line.append(f"{indent}  + {node['key']}: ")
                line.append(f"{iter_(node['children'][1])}")
            elif node['type'] == 'deleted':
                line.append(f"{indent}  - {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'added':
                line.append(f"{indent}  + {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            print(f"{line=}")
            result = itertools.chain('{', '\n', line, '\n', indent, '}')
            return ''.join(result)

        for nod_ in nods:
            if not isinstance(nod_, dict):
                return nod_
            string += iter_(nod_, depth)
        return string

    return build_string(tree_differences)


total = stylish('json_files/file1_stylish.json', 'json_files/file2_stylish.json')
string = open('json_files/file_out_2', 'w')
string.write(total)
print(total)
