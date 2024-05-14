from gendiff.formatters.make_str import to_str

# эта функция форматирует список потомков в нужный вид


def format_children(children):
    new_children = []
    for child in children:
        if child in (False, True, None) or isinstance(child, int):
            new_children.append(to_str(child))
        elif isinstance(child, dict):
            new_children.append('[complex value]')
        else:
            new_children.append(f"'{child}'")
    return new_children


def plain(tree_differences):

    def build_text(tree, path=''):
        nods = tree['children']

        def iter_(node, path_):
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
                return None
            elif node['type'] == 'added':
                children = format_children(node['children'])
                value = children[0]
                return f"Property '{path_[1:]}' was added with value: {value}"

        text = map(lambda node: iter_(node, path), nods)

        # эта функция удаляет результаты обхода словарей 'unchanged'
        def is_mutable(text_):
            return filter(lambda x: x is not None, text_)

        return "\n".join(is_mutable(text))

    return build_text(tree_differences)
