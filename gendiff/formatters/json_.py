from gendiff.make_tree import build_tree
import json
import yaml
from yaml.loader import SafeLoader


def json_(data1, data2):

    tree_differences = build_tree(data1, data2)


    result = json.dumps(tree_differences, default=lambda x: x.__dict__)

    return result

data1 = yaml.load(open('fixtures/nest_f1.yaml'), Loader=SafeLoader)
data2 = yaml.load(open('fixtures/nest_f2.yaml'), Loader=SafeLoader)


print(json_(data1, data2))
