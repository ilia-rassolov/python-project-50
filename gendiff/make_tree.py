
# эта функция создаёт внутреннее представление - промежуточную структуру данных tree_differences,
# где указаны различия между data1 и data2 по параметрам: ключ, тип изменения, значения по ключу


def build_tree(data_input, data_out):

    # эта функция формирует потомков из 2-х словарей по всем ключам

    def inner(data1, data2, not_comparable=False):
        children_tree = []
        keys = list(set(data1 | data2))
        keys.sort()

        # эта функция формирует список потомков из словарей по указанному ключу,
        # но только в том случае, если хотя бы один из потомков не словарь

        def build_children(dict1_, dict2_, key_):
            children_ = []
            for dict_ in (dict1_, dict2_):
                if key_ in dict_:
                    if isinstance(dict_[key_], dict):
                        value_ = inner(dict_[key_], dict_[key_], True)
                    else:
                        value_ = [dict_[key_]]
                    # в этом списке не должно быть дублированных значений
                    if value_ not in children_:
                        children_.extend(value_)
            return children_

        for key in keys:
            current_dict = {}
            current_dict['key'] = key
            value1 = data1.get(key)
            value2 = data2.get(key)

            if not_comparable:
                current_dict['type'] = 'not_comparable'
                if isinstance(value1, dict):
                    current_dict['children'] = inner(value1, value2, True)
                else:
                    current_dict['children'] = build_children(data1, data2, key)

            elif value1 == value2 and key in data1 and key in data2:
                current_dict['type'] = 'unchanged'
                if isinstance(value1, dict):
                    current_dict['children'] = inner(value1, value2)
                else:
                    current_dict['children'] = [value1]

            elif isinstance(value1, dict) and isinstance(value2, dict):
                current_dict['children'] = inner(value1, value2)
                current_dict['type'] = 'nested'
            elif key not in data1:
                current_dict['type'] = 'added'
                current_dict['children'] = build_children(data1, data2, key)
            elif key not in data2:
                current_dict['type'] = 'removed'
                current_dict['children'] = build_children(data1, data2, key)
            else:
                current_dict['type'] = 'updated'
                current_dict['children'] = build_children(data1, data2, key)

            children_tree.append(current_dict)
        return children_tree
    return {'type': 'root', 'children': inner(data_input, data_out)}
