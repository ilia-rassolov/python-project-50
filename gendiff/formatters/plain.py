from gendiff.make_str import to_str


def format_dict_value(dict_value):
    correct_value = dict_value[0]
    if correct_value in (False, True, None) or isinstance(correct_value, int):
        return to_str(correct_value)
    elif isinstance(correct_value, dict):
        return '[complex value]'
    else:
        return f"'{correct_value}'"


def format_simply(tree, path=''):
    if 'root' in tree:
        nods = tree['root']
    else:
        nods = tree['children']

    def walk(node, path_):
        path_ += f"{node['key']}."
        if node['type'] == 'nested':
            return format_simply(node, path_)
        elif node['type'] == 'updated':
            value = format_dict_value(node['value'])
            new_value = format_dict_value(node['new_value'])
            return f"Property '{path_[:-1]}' was updated. From {value} to {new_value}"
        elif node['type'] == 'removed':
            return f"Property '{path_[:-1]}' was removed"
        elif node['type'] == 'added':
            value = format_dict_value(node['value'])
            return f"Property '{path_[:-1]}' was added with value: {value}"

    text = [walk(node, path) for node in nods if walk(node, path)]
    return "\n".join(text)
