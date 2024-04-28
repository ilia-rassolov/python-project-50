import json
import yaml
from yaml.loader import SafeLoader


# эта функция извлекает данные из .json .yaml и .yml файлов
def parsing_file(filepath):
    if f'{filepath}'[-5:] == '.json':
        data = json.load(open(filepath))
    elif f'{filepath}'[-5:] == '.yaml' or f'{filepath}'[-4:] == '.yml':
        data = yaml.load(open(filepath), Loader=SafeLoader)
    else:
        string = open(filepath)
        data = string.read()
    return data
