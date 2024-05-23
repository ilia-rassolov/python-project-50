import json
import yaml
from yaml.loader import SafeLoader
from os import path


def parse_file(filepath):
    file_format = path.splitext(filepath)[-1]
    data = open(filepath)

    if file_format == '.json':
        return json.load(data)
    elif file_format == '.yaml' or file_format == '.yml':
        return yaml.load(data, Loader=SafeLoader)
    else:
        raise ValueError(f"Not correct file format: {file_format}")
