from gendiff.parser_file import parsing_file
from gendiff.dict_val_formatter import to_str

# эта функция создаёт внутреннее представление - промежуточную структуру данных tree_differences,
# где указаны различия между data1 и data2 по параметрам: ключ, тип изменения, значения по ключу


def build_tree(data1, data2):
    keys = list(set(data1 | data2))
    keys.sort()
    # print(f"{keys=}")
    tree_differences = []

    # эта функция формирует потомков из словарей по единому ключу,
    # но только в том случае, если эти потомки оба не словари

    def build_children(dict1_, dict2_, key_):
        children_ = []
        for dict_ in (dict1_, dict2_):
            if key_ in dict_:
                if isinstance(dict_[key_], dict):
                    value_ = build_tree(dict_[key_], dict_[key_])
                else:
                    value_ = [to_str(dict_[key_])]
                children_.extend(value_)
        # print(f"{children_=}")
        return children_

    for key in keys:
        # print(f"{key=}")
        current_dict = {}
        current_dict['key'] = key
        value1 = data1.get(key, 'absent')
        value2 = data2.get(key, 'absent')

        # print(f"{value1=}", f"{value2=}")

        if isinstance(value1, dict) and isinstance(value2, dict):
            if value1 == value2:
                current_dict['type'] = 'unchanged'
            else:
                current_dict['type'] = 'nested'
            current_dict['children'] = build_tree(value1, value2)

        else:
            # print(f'{data1=}')
            # print(f'{data2=}')
            current_dict['children'] = build_children(data1, data2, key)
            if value1 == value2:
                current_dict['type'] = 'unchanged'
                # print(f"{current_dict=}")
            elif value1 == 'absent':
                current_dict['type'] = 'added'
            elif value2 == 'absent':
                current_dict['type'] = 'deleted'
            else:
                current_dict['type'] = 'changed'
        # print(f"{current_dict=}")
        tree_differences.append(current_dict)
    return tree_differences


def stylish(filepath1_, filepath2_):
    data1 = parsing_file(filepath1_)
    data2 = parsing_file(filepath2_)

    # print('data1 = ', data1)
    # print('data2 = ', data2)

    tree_differences = build_tree(data1, data2)
    print(f"{tree_differences=}")

# эта функция накапливает результирующую строку

    def build_string(tree, depth=0):
        result = '{\n'

        # эта функция обрабатывает словари из внутреннего представления

        def iter_(node, depth_=0):
            if not isinstance(node, dict):
                return to_str(node)

            print(f"{node=}")
            indent = ' ' * 4 * depth_
            current_string = ''
            current_string += f"{indent}"

            # эта функция формирует потомков из словаря,
            # но только в том случае, если эти потомки оба не словари
            def get_children(dict_, depth_child):
                descendants = dict_['children']
                new_descendants = []
                for child in descendants:
                    print(f"{child=}")
                    if isinstance(child, dict):
                        depth_child += 1
                        print(f"{depth_child=}")
                        value_ = iter_(child, depth_child)
                    else:
                        value_ = to_str(child)
                    new_descendants.append(value_)
                    print(f"{new_descendants=}")
                return new_descendants

            children_node = node['children']
            if node['type'] == 'nested':
                current_string += f"    {node['key']}: "
                # children_node = node['children']
                current_string += f"{build_string(children_node, depth_ + 1)}\n"
            elif node['type'] == 'unchanged':
                current_string += f"    {node['key']}: {get_children(node, depth_)[0]}\n"
            elif node['type'] == 'changed':
                current_string += f"  - {node['key']}: {get_children(node, depth_)[0]}\n"
                current_string += f"{indent}  + {node['key']}: {get_children(node, depth_)[1]}\n"
            elif node['type'] == 'deleted':
                current_string += f"  - {node['key']}: "
                children_node = get_children(node, depth_)
                string_nest = '\n'.join(children_node)
                current_string += string_nest
                current_string += '\n'
            elif node['type'] == 'added':
                current_string += f"  + {node['key']}: "
                children_node = get_children(node, depth_)
                string_nest = '\n'.join(children_node)
                current_string += string_nest
                current_string += '\n'
            current_string += ''
            return current_string

        for node_ in tree:
            if isinstance(node_, dict):
                string = iter_(node_, depth)
                result += string
        result += f"{' ' * 4 * depth}"
        result += '}'
        return result

    return build_string(tree_differences)



total = stylish('json_files/file1_stylish.json', 'json_files/file2_stylish.json')
string = open('json_files/file_out_2', 'w')
string.write(total)
print(total)
