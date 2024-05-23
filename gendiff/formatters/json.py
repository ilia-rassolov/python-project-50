import json


def format_json(tree_differences):
    return json.dumps(tree_differences, indent=2, separators=(',', ':'))
