import json
import yaml
from yaml.loader import SafeLoader


# эта функция извлекает данные из .json .yaml и .yml файлов
def parsing_file(filepath):

    if f'{filepath}'[-5:] == '.json':
        return json.load(open(filepath))
    elif f'{filepath}'[-5:] == '.yaml' or f'{filepath}'[-4:] == '.yml':
        return yaml.load(open(filepath), Loader=SafeLoader)
    else:
        return 'Not correct request'
