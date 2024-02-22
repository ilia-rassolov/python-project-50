from parser_file import parsing_file

def generate_diff(filepath1_, filepath2_):
    data1_ = parsing_file(filepath1_)
    data2_ = parsing_file(filepath2_)

    # объединим ключи через множество в список
    keys = list(set(list(data1_.keys())
                    + list(data2_.keys())))
    keys.sort()

    # эта функция форматирует значения словарей в строки
    def to_str_value(data):
        data_str = {}
        for key in data.keys():
            if isinstance(data[key], bool):
                data_str[key] = str(data[key]).lower()
                # print('data_str[key] = ', data_str[key])
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
