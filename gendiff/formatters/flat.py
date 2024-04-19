from gendiff.formatters.make_str import to_str


def format_flat_data(data1, data2):
    # объединим ключи через множество в список
    keys = list(set(data1 | data2))
    keys.sort()

    # запишем различия между данными в строку
    result = '{\n'
    for key in keys:
        if key in data1:
            if key in data2:
                if data1[key] == data2[key]:
                    result += f'    {key}: {to_str(data1[key])}\n'
                else:
                    result += f'  - {key}: {to_str(data1[key])}\n'
                    result += f'  + {key}: {to_str(data2[key])}\n'
            else:
                result += f'  - {key}: {to_str(data1[key])}\n'
        else:
            result += f'  + {key}: {to_str(data2[key])}\n'
    result += '}'
    return result
