# эта функция форматирует потомков в нужный вид

def format_children(children):
    new_children = []
    for child in children:
        if child in ('false', 'true', 'null') or isinstance(child, int):
            new_children.append(child)
        elif isinstance(child, dict):
            new_children.append('[complex value]')
        else:
            new_children.append(f"'{child}'")
    return new_children
