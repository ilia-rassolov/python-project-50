from gendiff.make_tree import build_tree
from gendiff.parser_file import parsing_file
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)
    tree_differences = build_tree(data1, data2)
    if format_name == 'stylish':
        return stylish(tree_differences)
    elif format_name == 'plain':
        return plain(tree_differences)
    elif format_name == 'json':
        return json_(tree_differences)
    else:
        raise ValueError(f"Not correct formatter name: {format_name}")
