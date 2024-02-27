from gendiff.parser_file import parsing_file


def generate_diff(filepath1_, filepath2_):
    data1_: dict = parsing_file(filepath1_)
    data2_: dict = parsing_file(filepath2_)

    # объединим ключи через множество в список
    keys = list(set(list(data1_)
                    + list(data2_)))
    # print('keys = ', keys)
    keys.sort()

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

    data1_str = to_str_value(data1_)
    data2_str = to_str_value(data2_)

    # запишем различия между данными в строку
    result = '{\n'
    for key in keys:
        if key in data1_str:
            if key in data2_str:
                if data1_str[key] == data2_str[key]:
                    result += f'    {key}: {data1_str[key]}\n'
                else:
                    result += (f'  - {key}: {data1_str[key]}\n  + '
                               f'{key}: {data2_str[key]}\n')
            else:
                result += f'  - {key}: {data1_str[key]}\n'
        else:
            result += f'  + {key}: {data2_str[key]}\n'
    result += '}'

    return result
