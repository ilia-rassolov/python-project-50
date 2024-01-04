import argparse
import pathlib
import json


# parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
# parser.add_argument('first_file', type=pathlib.Path)
# parser.add_argument('second_file', type=pathlib.Path)
# parser.add_argument('-f', '--format', help='set format of output')
#
# args = parser.parse_args()

# def sample(first_file):
#     f = json.load(open(first_file))
#     print(f, ', host = ', f['host'])
#     for l in f:
#         print(l)
#
# sample('/home/user/PycharmProjects/HexletEx/py-pr-50/files/file1.json')

def generate_diff(first_file, second_file):

    data1 = json.load(open(first_file))
    data2 = json.load(open(second_file))
    print('data1 = ', data1)
    print('data2 = ', data2)

    keys = list(set(list(data1.keys()) + list(data2.keys()))) # объединяем ключи через множество в список
    keys.sort()
    print('keys = ', keys)

    diff = open("/home/user/PycharmProjects/HexletEx/py-pr-50/files/diff_file", "w")
    diff.write('{\nHello')
    diff.write('\nHello, World!')
    diff.write('\n}')
    diff_r = open("/home/user/PycharmProjects/HexletEx/py-pr-50/files/diff_file")
    for l in diff_r:
        print(l)
    d = diff_r.read()
    print(d)


    # result = open("/home/user/PycharmProjects/HexletEx/py-pr-50/files/diff_file")
    #
    # print(result)


    # for k in keys_sorted:






generate_diff('/home/user/PycharmProjects/HexletEx/py-pr-50/files/file1.json',
           '/home/user/PycharmProjects/HexletEx/py-pr-50/files/file2.json')




