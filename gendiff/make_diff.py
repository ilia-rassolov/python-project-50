from gendiff.parser_file import parsing_file
from gendiff.formatters.flat import flat
from gendiff.formatters.stylish import stylish


def generate_diff(filepath1, filepath2, format=stylish):
    # if format not in (flat, stylish):
    #     raise Exception('not correct name formatter')
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)
    return format(data1, data2)
