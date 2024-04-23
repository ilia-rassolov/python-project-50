from gendiff.make_tree import build_tree


def stylish(data1, data2):

    tree_differences = build_tree(data1, data2)
    # print(f"{tree_differences=}")

    # эта функция формирует результирующую строку-дифф

    def build_string(tree, depth=0):
        if not isinstance(tree, dict):
            return tree
        nods = tree['children']
        indent = ' ' * 4 * depth

        # эта функция обходит потомков и возвращает разницу между элементами данных

        def iter_(node, depth_=0):
            if not isinstance(node, dict):
                return node
            indent_ = ' ' * 4 * depth_
            line = ['\n']
            if node['type'] == 'nested':
                line.append(f"{indent_}    {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'unchanged':
                line.append(f"{indent_}    {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'changed':
                [value_in, value_out] = node['children']
                line.append(f"{indent_}  - {node['key']}: ")
                if isinstance(value_in, dict):
                    node['children'] = [value_in]
                line.append(f"{build_string(node, depth_ + 1)}\n")
                line.append(f"{indent_}  + {node['key']}: ")
                node['children'] = [value_out]
                if isinstance(value_out, dict):
                    node['children'] = [value_out]
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'deleted':
                line.append(f"{indent_}  - {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'added':
                line.append(f"{indent_}  + {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            return ''.join(line)

        string = '{'
        for node in nods:
            if not isinstance(node, dict):
                return node
            string += iter_(node, depth)
        string += f"\n{indent}"
        string += '}'
        return string

    return build_string(tree_differences)
