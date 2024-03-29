# from gendiff.make_diff import generate_diff
from gendiff.parser_file import parsing_file
from gendiff.dict_val_formatter import to_str

# эта функция создаёт внутреннее представление - промежуточную структуру данных tree_differences,
# где указаны различия между data1 и data2 по параметрам: ключ, тип изменения, значения по ключу


def build_tree(data1, data2):
    keys = list(set(data1 | data2))
    keys.sort()
    # print(f"{keys=}")
    tree_differences = []
    for key in keys:
        current_dict = {}
        current_dict['key'] = key
        if key in data1:
            if key in data2:
                value1 = data1[key]
                value2 = data2[key]
                if isinstance(value1, dict) and isinstance(value2, dict):
                    current_dict['type'] = 'nested'
                    current_dict['children'] = build_tree(value1, value2)
                elif value1 == value2:
                    current_dict['type'] = 'unchanged'
                    current_dict['children'] = [to_str(value1)]
                else:
                    current_dict['type'] = 'changed'
                    current_dict['children'] = [to_str(value1), to_str(value2)]
            else:
                current_dict['type'] = 'deleted'
                current_dict['children'] = [to_str(data1[key])]
        else:
            current_dict['type'] = 'added'
            current_dict['children'] = [to_str(data2[key])]
        tree_differences.append(current_dict)
    return tree_differences


def get_children(dict_):
    return dict_['children']


def stylish(filepath1_, filepath2_):
    data1 = parsing_file(filepath1_)
    data2 = parsing_file(filepath2_)

    print('data1 = ', data1)
    print('data2 = ', data2)

    tree_differences = build_tree(data1, data2)
    print(f"{tree_differences=}")

# эта функция создаёт результирующую строку

    def build_string(tree_list):
        result = ''


# эта функция словари из внутреннего представления
        def inner(node, depth=0):
            print(f"{node=}")
            indent = ' ' * 4 * depth
            current_string = f"{indent}"
            current_string += '{\n'
            if node['type'] == 'nested':
                children = get_children(node)
                print(f"{children=}")
                current_string += f"{indent}    {node['key']}: "
                for child in children:
                    depth += 1
                    print(f"{depth=}")
                    print(f"{child=}")
                    return inner(child)
            elif node['type'] == 'unchanged':
                current_string += f"{indent}    {node['key']}: {get_children(node)}\n"
            elif node['type'] == 'changed':
                current_string += f"{indent}  - {node['key']}: {get_children(node)[0]}\n"
                current_string += f"{indent}  + {node['key']}: {get_children(node)[1]}\n"
            elif node['type'] == 'deleted':
                current_string += f"{indent}  - {node['key']}: {get_children(node)[0]}\n"
            elif node['type'] == 'added':
                current_string += f"{indent}  + {node['key']}: {get_children(node)[0]}\n"
            current_string += f"{indent}"
            current_string += '}\n'
            print(f"{current_string=}")
            return current_string

        for item in tree_list:
            string = inner(item)
            result += string
        return result

    return build_string(tree_differences)


print(f"{stylish('json_files/file1_stylish.json', 'json_files/file2_stylish.json')=}")
