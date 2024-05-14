import json


def json_(tree_differences):

    return json.dumps(tree_differences, indent=2, separators=(',', ':'))
