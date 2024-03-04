import json
import yaml
from yaml.loader import SafeLoader


# эта функция форматирует значения словарей в строки
def to_str_value(data: dict):
    data_str = {}
    for key in data:
        if isinstance(data[key], bool):
            data_str[key] = str(data[key]).lower()
        elif data[key] == 'null':
            data_str[key] = None
        else:
            data_str[key] = str(data[key])
    return data_str

# эта функция извлекает данные из .json .yaml и .yml файлов
def parsing_file(filepath):

    if f'{filepath}'[-5:] == '.json':
        data = json.load(open(filepath))
    elif f'{filepath}'[-5:] == '.yaml' or f'{filepath}'[-4:] == '.yml':
        data = yaml.load(open(filepath), Loader=SafeLoader)
    else:
        data = {}

    return to_str_value(data)


