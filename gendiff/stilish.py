from gendiff.make_diff import generate_diff
from gendiff.make_diff import generate_diff_node
from gendiff.parser_file import parsing_file
from gendiff.dict_val_formatter import to_str_value, to_str


data1 = parsing_file('json_files/file1_stilish.json')
data2 = parsing_file('json_files/file2_stilish.json')
print('data1 = ', data1)
print('data2 = ', data2)

# объединим ключи через множество в список
keys_data = list(set(data1 | data2))
keys_data.sort()
print('keys_data = ', keys_data)

def stilish(filepath1, filepath2):

    def iter_(current_value, level=0):
        if not isinstance(current_value, dict):
            return to_str(current_value), level
        acc = level + 1
        lines = []
        for k, v in current_value.items():

        return to_str_value(current_value), level + 1




