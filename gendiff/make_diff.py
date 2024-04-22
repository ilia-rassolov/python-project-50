from gendiff.parser_file import parsing_file
from gendiff.formatters.flat import flat
from gendiff.formatters.stylish import stylish


def generate_diff(filepath1, filepath2, formatter=stylish):
    if formatter != flat or formatter != stylish:
        raise Exception('not correct name formatter')
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)
    return formatter(data1, data2)
