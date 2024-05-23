def get_all_descendants(data1, data2):
    all_descendants = []
    keys = list(set(data1 | data2))
    keys.sort()

    for key in keys:
        current_dict = dict()
        current_dict['key'] = key
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2 and key in data1 and key in data2:
            current_dict['type'] = 'unchanged'
            current_dict['value'] = [value1]
        elif isinstance(value1, dict) and isinstance(value2, dict):
            current_dict['children'] = get_all_descendants(value1, value2)
            current_dict['type'] = 'nested'
        elif key not in data1:
            current_dict['type'] = 'added'
            current_dict['value'] = [value2]
        elif key not in data2:
            current_dict['type'] = 'removed'
            current_dict['value'] = [value1]
        else:
            current_dict['type'] = 'updated'
            current_dict['value'] = [value1]
            current_dict['new_value'] = [value2]
        all_descendants.append(current_dict)
    return all_descendants

# эта функция создаёт внутреннее представление - промежуточную структуру данных tree_differences,
# где указаны различия между data1 и data2 по параметрам: ключ, тип изменения, значения потомков


def build_tree(data_input, data_out):
    return {'root': get_all_descendants(data_input, data_out)}
