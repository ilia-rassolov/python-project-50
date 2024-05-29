from gendiff.make_str import to_str


def format_stylishly(tree, descendants=None, depth=0):
    if not isinstance(tree, dict):
        return to_str(tree)
    elif 'root' in tree:
        nods = tree['root']
    elif descendants:
        nods = tree[descendants]
    else:
        nods = [{k: v} for k, v in tree.items()]
    indent = ' ' * 4 * depth

    def walk(node, depth_=0):
        if not isinstance(node, dict):
            return to_str(node)
        indent_ = ' ' * 4 * depth_
        line = ['\n']
        if not node.get('type'):
            for key_ in node.keys():
                line.append(f"{indent_}    {key_}: ")
                line.append(f"{format_stylishly(node[key_], depth=depth_ + 1)}\n")
            line[-1] = line[-1][:-1]
        elif node['type'] == 'nested':
            line.append(f"{indent_}    {node['key']}: ")
            line.append(f"{format_stylishly(node, 'children', depth_ + 1)}")
        elif node['type'] == 'unchanged':
            line.append(f"{indent_}    {node['key']}: ")
            line.append(f"{format_stylishly(node, 'value', depth_ + 1)}")
        elif node['type'] == 'updated':
            line.append(f"{indent_}  - {node['key']}: ")
            line.append(f"{format_stylishly(node, 'value', depth_ + 1)}\n")
            line.append(f"{indent_}  + {node['key']}: ")
            line.append(f"{format_stylishly(node, 'new_value', depth_ + 1)}")
        elif node['type'] == 'removed':
            line.append(f"{indent_}  - {node['key']}: ")
            line.append(f"{format_stylishly(node, 'value', depth_ + 1)}")
        elif node['type'] == 'added':
            line.append(f"{indent_}  + {node['key']}: ")
            line.append(f"{format_stylishly(node, 'value', depth_ + 1)}")
        return ''.join(line)

    result = ['{']
    for node_ in nods:
        if not isinstance(node_, dict):
            return to_str(node_)
        result.append(walk(node_, depth))
    result.append(f"\n{indent}")
    result.append('}')
    return ''.join(result)
