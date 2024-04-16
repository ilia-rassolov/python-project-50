from gendiff.make_diff import generate_diff
from gendiff.parser_file import parsing_file
from gendiff.dict_val_formatter import to_str_value
from gendiff.stylish import build_tree, stylish

import pytest


# @pytest.mark.parametrize("filepath1", ['/home/mint/PycharmProjects/python-project-50/tests/fixtures/f1_input.json',
#                                        '/home/mint/PycharmProjects/python-project-50/tests/fixtures/f1_input.yaml',
#                                        '/home/mint/PycharmProjects/python-project-50/tests/fixtures/file.yml'])
# @pytest.mark.parametrize("filepath2", ['/home/mint/PycharmProjects/python-project-50/tests/fixtures/f2_input.json',
#                                        '/home/mint/PycharmProjects/python-project-50/tests/fixtures/f2_input.yaml'])
# def test_generate_diff(filepath1, filepath2):
#
#     data1: dict = parsing_file(filepath1)
#     data2: dict = parsing_file(filepath2)
#
#     # объединим ключи через множество в список
#     keys = list(set(data1 | data2))
#     keys.sort()
#
#     data1_str = to_str_value(data1)
#     data2_str = to_str_value(data2)
#
#     # запишем различия между данными в file_out и прочтём их
#     string = open('/home/mint/PycharmProjects/python-project-50/tests/fixtures/file_out', 'w')
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
#     string = open('/home/mint/PycharmProjects/python-project-50/tests/fixtures/file_out')
#     result = string.read()
#
#     diff = generate_diff(filepath1, filepath2)
#     assert diff == result
#     pass

@pytest.mark.parametrize("filepath1", ['/home/mint/PycharmProjects/python-project-50/tests/fixtures/f1_nest.json'])
#                                        # '/home/mint/PycharmProjects/python-project-50/tests/fixtures/f1_nest.yaml',
#                                        # '/home/mint/PycharmProjects/python-project-50/tests/fixtures/f1_nest.yml'])
@pytest.mark.parametrize("filepath2", ['/home/mint/PycharmProjects/python-project-50/tests/fixtures/f2_nest.json'])
#                                        # '/home/mint/PycharmProjects/python-project-50/tests/fixtures/f2_nest.yaml'])
def test_stylish(filepath1, filepath2):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)
    tree_differences = build_tree(data1, data2)
    print(f"{tree_differences=}")
    # запишем различия между данными в file_out и прочтём их

    def test_build_string(tree, depth=0):
        string = open('/home/mint/PycharmProjects/python-project-50/tests/fixtures/file_out', 'w')
        # print(f"{tree=}")
        if not isinstance(tree, dict):
            return tree
        nods = tree['children']
        indent = ' ' * 4 * depth

        def test_iter_(node, depth_=0):
            if not isinstance(node, dict):
                return node
            indent_ = ' ' * 4 * depth_
            string.write('\n')
            if node['type'] == 'nested':
                string.write(f"{indent_}    {node['key']}: ")
                string.write(f"{test_build_string(node, depth_ + 1)}")
            elif node['type'] == 'unchanged':
                string.write(f"{indent_}    {node['key']}: ")
                string.write(f"{test_build_string(node, depth_ + 1)}")
            elif node['type'] == 'changed':
                [value_in, value_out] = node['children']
                string.write(f"{indent_}  - {node['key']}: ")
                if isinstance(value_in, dict):
                    node['children'] = [value_in]
                string.write(f"{test_build_string(node, depth_ + 1)}\n")
                string.write(f"{indent_}  + {node['key']}: ")
                node['children'] = [value_out]
                if isinstance(value_out, dict):
                    node['children'] = [value_out]
                string.write(f"{test_build_string(node, depth_ + 1)}")
            elif node['type'] == 'deleted':
                string.write(f"{indent_}  - {node['key']}: ")
                string.write(f"{test_build_string(node, depth_ + 1)}")
            elif node['type'] == 'added':
                string.write(f"{indent_}  + {node['key']}: ")
                string.write(f"{test_build_string(node, depth_ + 1)}")
            # print(f"{line=}")
            # return ''.join(line)

        string.write('{')
        for node in nods:
            if not isinstance(node, dict):
                return node
            string.write(f"{test_iter_(node, depth)}")
        string.write(f"\n{indent}")
        string.write('}')

    test_build_string(tree_differences)

    string = open('/home/mint/PycharmProjects/python-project-50/tests/fixtures/file_out')
    result = string.read()

    diff = stylish(filepath1, filepath2)
    print(diff)
    assert diff == result




