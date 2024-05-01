from gendiff.parser_file import parsing_file
from gendiff.formatters.flat import flat
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_ import json_


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)
    if format_name == 'stylish':
        return stylish(data1, data2)
    elif format_name == 'flat':
        return flat(data1, data2)
    elif format_name == 'plain':
        return plain(data1, data2)
    elif format_name == 'json':
        return json_(data1, data2)
    else:
        raise ValueError(f"Not correct formatter name: {format_name}")

# f_p_1 = 'formatters/fixtures/nest_f1.json'
# f_p_2 = 'formatters/fixtures/nest_f2.json'
# print(generate_diff(f_p_1, f_p_2, 'plain'))
