# эта функция форматирует значения в строки
def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif value == 0:
        return value
    else:
        return value
