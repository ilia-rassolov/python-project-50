from gendiff.parser_file import parsing_file
from gendiff.formatters.flat import format_flat_data
from gendiff.formatters.stylish import stylish

def generate_diff(filepath1, filepath2, format=stylish):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)
    return format(data1, data2)
