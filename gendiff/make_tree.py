from gendiff.formatters.make_str import to_str

# эта функция создаёт внутреннее представление - промежуточную структуру данных tree_differences,
# где указаны различия между data1 и data2 по параметрам: ключ, тип изменения, значения по ключу


def build_tree(data_input, data_out):

    # эта функция формирует потомков из 2-х словарей по всем ключам

    def inner(data1, data2):
        children_tree = []
        keys = list(set(data1 | data2))
        keys.sort()

        # эта функция формирует потомков из словарей по указанному ключу,
        # но только в том случае, если эти потомки оба не словари

        def build_children(dict1_, dict2_, key_):
            children_ = []
            for dict_ in (dict1_, dict2_):
                if key_ in dict_:
                    if isinstance(dict_[key_], dict):
                        value_ = inner(dict_[key_], dict_[key_])
                    else:
                        value_ = [to_str(dict_[key_])]
                    children_.extend(value_)
            return children_

        for key in keys:
            # print(f"{key=}")
            current_dict = {}
            current_dict['key'] = key
            value1 = data1.get(key, 'absent')
            value2 = data2.get(key, 'absent')

            if isinstance(value1, dict) and isinstance(value2, dict):
                current_dict['children'] = inner(value1, value2)
                if value1 == value2:
                    current_dict['type'] = 'unchanged'
                else:
                    current_dict['type'] = 'nested'
            else:
                current_dict['children'] = build_children(data1, data2, key)
                if value1 == value2:
                    current_dict['type'] = 'unchanged'
                    # в этом списке устраним дублирование значений
                    current_dict['children'] = list(set(current_dict['children']))
                elif value1 == 'absent':
                    current_dict['type'] = 'added'
                elif value2 == 'absent':
                    current_dict['type'] = 'deleted'
                else:
                    current_dict['type'] = 'changed'

            children_tree.append(current_dict)
        return children_tree
    return {'type': 'root', 'children': inner(data_input, data_out)}
