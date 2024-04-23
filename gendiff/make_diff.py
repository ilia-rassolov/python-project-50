from gendiff.parser_file import parsing_file
from gendiff.formatters.flat import flat
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)
    if format_name == 'stylish':
        return stylish(data1, data2)
    if format_name == 'flat':
        return flat(data1, data2)
    if format_name == 'plain':
        return plain(data1, data2)
    else:
        raise ValueError(f"Not correct formatter name: {format_name}")
