from gendiff.make_tree import build_tree
from gendiff.parser_file import parsing_file
from gendiff.formatters.children_for_plain import format_children
from functools import reduce


# эта функция удаляет результат обхода словарей 'unchanged'
def filter_is_unchanged(text_):
    return filter(lambda x: x != 'empty line', text_)


def plain(data1, data2):

    tree_differences = build_tree(data1, data2)
    print(f"{tree_differences=}")

    def build_text(tree, path=''):
        nods = tree['children']

        def iter_(node, path_):
            # print(f"{node=}, {path_=}")
            path_ += f".{node['key']}"
            if node['type'] == 'nested':
                return build_text(node, path_)
            elif node['type'] == 'updated':
                children = format_children(node['children'])
                [value_in, value_out] = children
                return f"Property '{path_[1:]}' was updated. From {value_in} to {value_out}"
            elif node['type'] == 'removed':
                return f"Property '{path_[1:]}' was removed"
            elif node['type'] == 'unchanged':
                return 'empty line'
            elif node['type'] == 'added':
                children = format_children(node['children'])
                value = children[0]
                return f"Property '{path_[1:]}' was added with value: {value}"

        text = reduce(lambda acc, node: acc + [iter_(node, path)], nods, [])
        return "\n".join(filter_is_unchanged(text))

    return build_text(tree_differences)


data1 = parsing_file('fixtures/nest_f1.json')
data2 = parsing_file('fixtures/nest_f2.json')

print(plain(data1, data2))
