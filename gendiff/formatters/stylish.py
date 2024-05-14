from gendiff.formatters.make_str import to_str


def stylish(tree_differences):

    def build_string(tree, depth=0):
        if not isinstance(tree, dict):
            return tree
        nods = tree['children']
        indent = ' ' * 4 * depth

        # эта функция обходит потомков и возвращает разницу между элементами данных

        def iter_(node, depth_=0):
            if not isinstance(node, dict):
                return to_str(node)
            indent_ = ' ' * 4 * depth_
            line = ['\n']
            if node['type'] == 'nested':
                line.append(f"{indent_}    {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'unchanged':
                line.append(f"{indent_}    {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'updated':
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
            elif node['type'] == 'removed':
                line.append(f"{indent_}  - {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            elif node['type'] == 'added':
                line.append(f"{indent_}  + {node['key']}: ")
                line.append(f"{build_string(node, depth_ + 1)}")
            return ''.join(line)

        string = '{'
        for node in nods:
            if not isinstance(node, dict):
                return to_str(node)
            string += iter_(node, depth)
        string += f"\n{indent}"
        string += '}'
        return string

    return build_string(tree_differences)
