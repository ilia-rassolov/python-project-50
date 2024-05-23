
# эта функция создаёт внутреннее представление - промежуточную структуру данных tree_differences,
# где указаны различия между data1 и data2 по параметрам: ключ, тип изменения, значения по ключу


def build_tree(data_input, data_out):

    # эта функция формирует потомков из 2-х словарей по всем ключам

    def inner(data1, data2):
        children_tree = []
        keys = list(set(data1 | data2))
        keys.sort()

        for key in keys:
            current_dict = {}
            current_dict['key'] = key
            value1 = data1.get(key)
            value2 = data2.get(key)

            if value1 == value2 and key in data1 and key in data2:
                current_dict['type'] = 'unchanged'
                current_dict['value'] = [value1]
            elif isinstance(value1, dict) and isinstance(value2, dict):
                current_dict['children'] = inner(value1, value2)
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

            children_tree.append(current_dict)
        return children_tree
    return {'root': inner(data_input, data_out)}
