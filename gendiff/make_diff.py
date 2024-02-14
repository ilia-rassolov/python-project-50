import json


def generate_diff(filepath1, filepath2):

    data1 = json.load(open(filepath1))
    data2 = json.load(open(filepath2))

    # объединим ключи через множество в список
    keys = list(set(list(data1.keys())
                    + list(data2.keys())))
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

    data1_str = to_str_value(data1)
    data2_str = to_str_value(data2)

    # print('data1_str = ', data1_str)
    # print('data2_str = ', data2_str)

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

#
# print(generate_diff('json_files/file1.json', 'json_files/file2.json'))
#
# print(generate_diff('/home/mint/PycharmProjects/python-project-50/tests/fixtures/f1_input.json',
#                     '/home/mint/PycharmProjects/python-project-50/tests/fixtures/f2_input.json'))
