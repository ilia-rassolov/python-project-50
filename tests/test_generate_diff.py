from gendiff.make_diff_flat import generate_diff
from gendiff.parser_file import parsing_file
from gendiff.formatters.make_str import to_str_value
import pytest


@pytest.mark.parametrize("filepath1", ['fixtures/flat_f1.json',
                                       'fixtures/flat_f1.yaml',
                                       'fixtures/flat_f1.yml'])
@pytest.mark.parametrize("filepath2", ['fixtures/flat_f2.json',
                                       'fixtures/flat_f2.yaml'])
def test_generate_diff(filepath1, filepath2):

    data1: dict = parsing_file(filepath1)
    data2: dict = parsing_file(filepath2)

    # объединим ключи через множество в список
    keys = list(set(data1 | data2))
    keys.sort()

    data1_str = to_str_value(data1)
    data2_str = to_str_value(data2)

    # запишем различия между данными в exp_flat и прочтём их
    string = open('fixtures/exp_flat', 'w')
    string.write('{\n')
    for key in keys:
        # print(key)
        if key in data1_str:
            if key in data2_str:
                if data1_str[key] == data2_str[key]:
                    string.write(f'    {key}: {data1_str[key]}\n')
                else:
                    string.write(f'  - {key}: {data1_str[key]}\n  + {key}: {data2_str[key]}\n')
            else:
                string.write(f'  - {key}: {data1_str[key]}\n')
        else:
            string.write(f'  + {key}: {data2_str[key]}\n')
    string.write('}')
    string = open('fixtures/exp_flat')
    expected_result = string.read()

    diff = generate_diff(filepath1, filepath2)
    assert diff == expected_result
    pass
