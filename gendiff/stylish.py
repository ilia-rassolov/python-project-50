from make_diff import generate_diff_node
from parser_file import parsing_file


def stylish(filepath1_, filepath2_):

    data1: dict = parsing_file(filepath1_)
    data2: dict = parsing_file(filepath2_)
    print('data1 = ', data1)
    print('data2 = ', data2)

    # объединим ключи через множество в список
    keys_data = list(set(data1 | data2))
    keys_data.sort()
    print('keys_data = ', keys_data)

    # запишем различия между данными в file_out и прочтём их
    string = open('fixtures/file_out', 'w')
    string.write('{\n')
    def inner(node1, node2, keys_inner=keys_data, level=1):
        for key in keys_inner:
            print('key =', key)
            if key in node1:
                if key in node2:
                    string.write(f"{' ' * (level * 4 - 2)}{key}")
                    string.write(': {\n')
                    value1, value2, acc = generate_diff_node(node1, node2, key, level)
                    print('value1 = ', value1, type(value1), type(value2))
                    if not isinstance(value1, dict) and not isinstance(value2, dict):
                        print('value1 = ', value1, 'value2 = ', value2, 'acc = ', acc)
                        if value1 == value2:
                            string.write(f"{' ' * (acc * 4 - 2)}{key}: {value1}\n")
                        else:
                            string.write(f"{'  - ' * acc}{key}: {value1}\n")
                            string.write(f"{'  + ' * acc}{key}: {value2}\n")
                    else:
                        children1, children2 = value1, value2
                        print('children1 = ', children1, 'children2 = ', children2)
                        keys_children = list(set(children1 | children2))
                        keys_children.sort()
                        print('keys_children = ', keys_children, acc)
                        inner(children1, children2, keys_children, acc)
                else:
                    string.write(f"{'  - ' * level}{key}: {node1[key]}\n")
            else:
                string.write(f"{'    ' * (level - 1)}{'  + '}{key}: {node2[key]}\n")
            string.write(f"{'    ' * level}")
        string.write('}\n')
    inner(data1, data2)
    string = open('fixtures/file_out')
    result = string.read()
    print(result)
    # diff = generate_diff('fixtures/file1_stilish.json', 'fixtures/file2_stilish.json')
    # assert diff == result
    # pass

# data1_str = {'host': 'hexlet.io', 'timeout': '50', 'proxy': '123.234.53.22', 'follow': 'false'}
# data2_str = {'timeout': '20', 'verbose': 'true', 'host': 'hexlet.io'}
# print(generate_diff_key('proxy'))
print(test_generate_diff())