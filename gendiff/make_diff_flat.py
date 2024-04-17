from gendiff.parser_file import parsing_file
from gendiff.formatters.make_str import to_str_value


def generate_diff(filepath1_, filepath2_):
    data1: dict = parsing_file(filepath1_)
    data2: dict = parsing_file(filepath2_)
    data1_ = to_str_value(data1)
    data2_ = to_str_value(data2)
    print(data1_, data2_)

    # объединим ключи через множество в список
    keys = list(set(data1_ | data2_))
    keys.sort()

    # запишем различия между данными в строку
    result = '{\n'
    for key in keys:
        if key in data1_:
            if key in data2_:
                if data1_[key] == data2_[key]:
                    result += f'    {key}: {data1_[key]}\n'
                else:
                    result += f'  - {key}: {data1_[key]}\n'
                    result += f'  + {key}: {data2_[key]}\n'
            else:
                result += f'  - {key}: {data1_[key]}\n'
        else:
            result += f'  + {key}: {data2_[key]}\n'
    result += '}'
    return result
