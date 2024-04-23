from gendiff.make_tree import build_tree
from gendiff.parser_file import parsing_file
from gendiff.formatters.make_str import to_str


def plain(data1, data2):

    tree_differences = build_tree(data1, data2)
    print(f"{tree_differences=}")

    def build_text(tree):
        nods = tree['children']
        text = []

        # эта функция обходит потомков и возвращает описание изменений значений

        def iter_(node):
            print(f"{node=}")
            if not isinstance(node, dict):
                return node
            line = ['Property ']
            if node['type'] == 'nested':
                line.append(f"'{node['key']}'{build_text(node)}")
            elif node['type'] == 'unchanged':
                line = []
            elif node['type'] == 'changed':
                [value_in, value_out] = node['children']
                line.append(f"'{node['key']}' was updated. From ")
                if isinstance(value_in, dict):
                    value_in = '[complex value]'
                line.append(f"{value_in} to ")
                if isinstance(value_out, dict):
                    value_out = '[complex value]'
                line.append(value_out)
            elif node['type'] == 'deleted':
                line.append(f"'{node['key']}' was removed")
            elif node['type'] == 'added':
                [value] = node['children']
                if isinstance(value, dict):
                    value = '[complex value]'
                line.append(f"'{node['key']}' was added with value: {value}")
            return ''.join(line)

        for node in nods:

            if not isinstance(node, dict):
                return node
            text.extend(iter_(node))
        return 'Property ' + "\n'Property '".join(text)

    return build_text(tree_differences)








data1 = parsing_file('fixtures/nest_f1.json')
data2 = parsing_file('fixtures/nest_f2.json')

print(plain(data1, data2))