from gendiff.make_diff import generate_diff
from gendiff.parser_file import parsing_file
from gendiff.formatters.make_str import to_str
from gendiff.formatters.stylish import stylish
import pytest


@pytest.mark.parametrize("filepath1", ['fixtures/flat_f1.json',
                                       'fixtures/flat_f1.yaml',
                                       'fixtures/flat_f1.yml'])
@pytest.mark.parametrize("filepath2", ['fixtures/flat_f2.json',
                                       'fixtures/flat_f2.yaml'])
def test_generate_diff(filepath1, filepath2, format=stylish):

    data1 = parsing_file(filepath1)
    data2 = parsing_file(filepath2)

    if format != stylish:

        # объединим ключи через множество в список
        keys = list(set(data1 | data2))
        keys.sort()

        # запишем различия между данными в exp_flat и прочтём их
        string = open('fixtures/exp_flat', 'w')
        string.write('{\n')
        for key in keys:
            # print(key)
            if key in data1:
                if key in data2:
                    if data1[key] == data2[key]:
                        string.write(f'    {key}: {to_str(data1[key])}\n')
                    else:
                        string.write(f'  - {key}: {to_str(data1[key])}\n  + {key}: {to_str(data2[key])}\n')
                else:
                    string.write(f'  - {key}: {to_str(data1[key])}\n')
            else:
                string.write(f'  + {key}: {to_str(data2[key])}\n')
        string.write('}')
        string = open('fixtures/exp_flat')
        expected_result = string.read()

        diff = generate_diff(filepath1, filepath2, format)
        assert diff == expected_result
        pass
    else:



