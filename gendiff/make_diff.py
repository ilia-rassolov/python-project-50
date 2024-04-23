from gendiff.parser_file import parsing_file
from gendiff.formatters.flat import flat
from gendiff.formatters.stylish import stylish


def generate_diff(filepath1, filepath2, formatter='stylish'):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)
    if formatter == 'stylish':
        return stylish(data1, data2)
    if formatter == 'flat':
        return flat(data1, data2)
    else:
        raise ValueError(f"Not correct formatter name: {formatter}")
