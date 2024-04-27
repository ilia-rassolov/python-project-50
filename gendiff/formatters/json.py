from gendiff.make_tree import build_tree
import json


def json_(data1, data2):

    tree_differences = build_tree(data1, data2)

    return json.dumps(tree_differences, indent='..', separators=(',', ':'), sort_keys=False)
