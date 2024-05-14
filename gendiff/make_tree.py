
# эта функция создаёт внутреннее представление - промежуточную структуру данных tree_differences,
# где указаны различия между data1 и data2 по параметрам: ключ, тип изменения, значения по ключу


def build_tree(data_input, data_out):

    # эта функция формирует потомков из 2-х словарей по всем ключам

    def inner(data1, data2):
        children_tree = []
        keys = list(set(data1 | data2))
        keys.sort()

        # эта функция формирует потомков из словарей по указанному ключу,
        # но только в том случае, если хотя бы один из потомков не словарь

        def build_children(dict1_, dict2_, key_):
            children_ = []
            for dict_ in (dict1_, dict2_):
                if key_ in dict_:
                    if isinstance(dict_[key_], dict):
                        value_ = inner(dict_[key_], dict_[key_])
                    else:
                        value_ = [dict_[key_]]
                    children_.extend(value_)
            return children_

        for key in keys:
            current_dict = {}
            current_dict['key'] = key
            value1 = data1.get(key)
            value2 = data2.get(key)

            if isinstance(value1, dict) and isinstance(value2, dict):
                current_dict['children'] = inner(value1, value2)
                if value1 == value2:
                    current_dict['type'] = 'unchanged'
                else:
                    current_dict['type'] = 'nested'
            else:
                current_dict['children'] = build_children(data1, data2, key)
                if value1 == value2 and key in data1 and key in data2:
                    current_dict['type'] = 'unchanged'
                    # в этом списке устраним дублирование значений
                    current_dict['children'] = list(set(current_dict['children']))
                elif key not in data1:
                    current_dict['type'] = 'added'
                elif key not in data2:
                    current_dict['type'] = 'removed'
                else:
                    current_dict['type'] = 'updated'

            children_tree.append(current_dict)
        return children_tree
    return {'type': 'root', 'children': inner(data_input, data_out)}

#
# data1 = {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value',
# 'doge': {'wow': ''}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2':
# {'abc': 12345, 'deep': {'id': 45}}}
# data2 = {'common': {'follow': False, 'setting1': 'Value 1', 'setting3': None, 'setting4': 'blah blah', 'setting5':
# {'key5': 'value5'}, 'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}}, 'group1':
# {'foo': 'bar', 'baz': 'bars', 'nest': 'str'}, 'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
# print(f"{data1=}")
# print(f"{data2=}")
# print(build_tree(data1, data2))
