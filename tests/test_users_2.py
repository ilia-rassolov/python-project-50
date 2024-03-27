from gendiff.parser_file import parsing_file
from gendiff.dict_val_formatter import to_str_value, to_str


# эта функция отвечает за внутреннее представление,

def generate_diff_node(key_, node1_, node2_):
    if key_ in node1_:
        if key_ in node2_:
            value_1 = node1_[key_]
            value_2 = node2_[key_]
            if value_1 == value_2:
                return (value_1, '    '), ({}, None)
            else:
                return (value_1, '  - '), (value_2, '  + ')
        else:
            return (node1_[key_], '  - '), ({}, None)
    else:
        return ({}, None), (node2_[key_], '  + ')


def test_generate_diff():

    data1_: dict = parsing_file('fixtures/file1.json')
    data2_: dict = parsing_file('fixtures/file2.json')
    data1 = to_str_value(data1_)
    data2 = to_str_value(data2_)

    # объединим ключи через множество в список
    keys_data = list(set(data1 | data2))
    keys_data.sort()

    # запишем различия между данными в file_out и прочтём их
    string = open('fixtures/file_out', 'w')

    def inner(node1, node2, keys_inner=keys_data, level=0):
        string.write(' ' * level)
        string.write('{\n')
        for key in keys_inner:
            (value1, symbol1), (value2, symbol2) = generate_diff_node(key, node1, node2)
            keys_children = []
            for val, symbol in ((value1, symbol1), (value2, symbol2)):
                if not isinstance(val, dict):
                    string.write(f"{'    ' * level}{symbol}{key}: {to_str(val)}\n")
                elif isinstance(val, dict) and val:
                    string.write(f"{'    ' * level}{symbol}{key}:")
                    children = val
                    keys_children.extend(list(children.keys()))
                    keys_children = list(set(keys_children))
                    keys_children.sort()
            if keys_children:
                level += 1
                inner(value1, value2, keys_children, level)
        string.write(' ' * level)
        string.write('}\n')
    inner(data1, data2)
    string = open('fixtures/file_out')
    result = string.read()
    return result
