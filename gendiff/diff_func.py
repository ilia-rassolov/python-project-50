import json


def generate_diff(first_file, second_file):

    data1 = json.load(open(first_file))
    data2 = json.load(open(second_file))

    # print('data1 = ', data1)
    # print('data2 = ', data2)

    keys = list(set(list(data1.keys()) + list(data2.keys())))  # объединяем ключи через множество в список
    keys.sort()
    # print('keys = ', keys)

    diff_str = open("diff_file", "w")
    diff_str.write('{\n')
    for key in keys:
        if key in data1:
            if key in data2:
                if data1[key] == data2[key]:
                    diff_str.write(f'    {key}: {data1[key]}\n')
                else:
                    diff_str.write(f'  - {key}: {data1[key]}\n  + {key}: {data2[key]}\n')
            else:
                diff_str.write(f'  - {key}: {data1[key]}\n')
        else:
            diff_str.write(f'  + {key}: {data2[key]}\n')
    diff_str.write('}')
    diff_str.close()
    diff_str = open("diff_file")
    # print(diff_str.read())
    return diff_str.read()


# generate_diff('file1.json',
#               'file2.json')
