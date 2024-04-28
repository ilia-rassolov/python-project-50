from gendiff.make_tree import build_tree
from gendiff.formatters.children_for_plain import format_children


def plain(data1, data2):

    tree_differences = build_tree(data1, data2)
    # print(f"{tree_differences=}")

    def build_text(tree, path=''):
        nods = tree['children']

        def iter_(node, path_):
            path_ += f".{node['key']}"
            if node['type'] == 'nested':
                return build_text(node, path_)
            elif node['type'] == 'updated':
                children = format_children(node['children'])
                # print(f"{children=}")
                [value_in, value_out] = children
                return f"Property '{path_[1:]}' was updated. From {value_in} to {value_out}"
            elif node['type'] == 'removed':
                return f"Property '{path_[1:]}' was removed"
            elif node['type'] == 'unchanged':
                return 'data is immutable'
            elif node['type'] == 'added':
                children = format_children(node['children'])
                value = children[0]
                return f"Property '{path_[1:]}' was added with value: {value}"

        text = map(lambda node: iter_(node, path), nods)

        # эта функция удаляет результаты обхода словарей 'unchanged'
        def is_mutable(text_):
            return filter(lambda x: x != 'data is immutable', text_)

        return "\n".join(is_mutable(text))

    return build_text(tree_differences)
