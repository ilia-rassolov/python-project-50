# эта функция форматирует значения словарей в строки

def to_str_value(data: dict):
    data_str = {}
    for key in data:
        if isinstance(data[key], bool):
            data_str[key] = str(data[key]).lower()
        elif data[key] == 'null':
            data_str[key] = None
        else:
            data_str[key] = data[key]
    return data_str


# эта функция форматирует значения в строки
def to_str(value):
    if isinstance(value, bool):
        value = str(value).lower()
    elif value == None:
        value = 'null'
    else:
        pass
    return str(value)

# abs = 'home/user/PycharmProjects/HexletEx/python-project-50/tests/'
