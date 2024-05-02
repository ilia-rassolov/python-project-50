from gendiff.make_tree import build_tree
import json


def json_(data1, data2):

    tree_differences = build_tree(data1, data2)
    print(f"{type(tree_differences)=}")
    # tree_differences = tree_differences.replace("\'", "\"")
    print(f"{tree_differences=}")

    return json.dumps(tree_differences, indent='..', separators=(',', ':'))
