from gendiff.make_diff import generate_diff
import json


def test_generate_diff():
    data1 = json.load(open('tests/fixtures/f1_input.json'))
    # print('data1 = ', data1)
    data2 = json.load(open('tests/fixtures/f2_input.json'))

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
            elif data[key] == 'null':
                data_str[key] = None
            else:
                data_str[key] = str(data[key])
        return data_str

    data1_str = to_str_value(data1)
    data2_str = to_str_value(data2)

    # запишем различия между данными в file_out и прочтём их
    string = open('tests/fixtures/file_out', 'w')
    string.write('{\n')
    for key in keys:
        # print(key)
        if key in data1_str:
            if key in data2_str:
                if data1_str[key] == data2_str[key]:
                    string.write(f'    {key}: {data1_str[key]}\n')
                else:
                    string.write(f'  - {key}: {data1_str[key]}\n  + {key}: {data2_str[key]}\n')
            else:
                string.write(f'  - {key}: {data1_str[key]}\n')
        else:
            string.write(f'  + {key}: {data2_str[key]}\n')
    string.write('}')
    string = open('tests/fixtures/file_out')
    result = string.read()

    assert generate_diff('tests/fixtures/f1_input.json', 'tests/fixtures/f2_input.json') == result
