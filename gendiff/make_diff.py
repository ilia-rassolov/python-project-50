from gendiff.make_tree import build_tree
from gendiff.parser_file import parse_file
from gendiff.formatters.stylish import format_stylishly
from gendiff.formatters.plain import format_simply
from gendiff.formatters.json import format_json


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)
    tree_differences = build_tree(data1, data2)

    if format_name == 'stylish':
        return format_stylishly(tree_differences)
    elif format_name == 'plain':
        return format_simply(tree_differences)
    elif format_name == 'json':
        return format_json(tree_differences)
    else:
        raise ValueError(f"Not correct formatter name: {format_name}")
