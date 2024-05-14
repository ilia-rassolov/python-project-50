import json
import yaml
from yaml.loader import SafeLoader


def parsing_file(filepath):
    data = open(filepath)
    file_format = filepath.split('.')[-1]

    def build_dict(data_, file_format_):
        if file_format_ == 'json':
            return json.load(data_)
        elif file_format_ == 'yaml' or file_format == 'yml':
            return yaml.load(data_, Loader=SafeLoader)
        else:
            raise ValueError(f"Not correct file format: {file_format}")
    return build_dict(data, file_format)
