def values_within_line_length(values, line_length):
    """Return a set with at least one value but with no additional values
    causing the representation to exceed line_length
    """
    values = values.copy()
    ex_values = {values.pop()}

    if values:
        next_values = ex_values | {values.pop()}
        while next_values and len(repr(next_values)) < line_length:
            ex_values = next_values
            if values:
                next_values = ex_values | {values.pop()}
            else:
                next_values = None

    return ex_values


def print_subtree(subtree, line_length, indent=''):
    print('{0}<{1}>'.format(indent, subtree.name))

    for attr, values in subtree.attr_values():
        prefix = '{0}  {1} = '.format(indent, attr)
        fk_prefix = ' '*(len(prefix) - 3) + '-> '

        ex_values = values_within_line_length(values, line_length - len(prefix))
        print('{0}{1}'.format(prefix, ex_values))

        for num, fk_path in sorted(subtree.foreign_keys[attr], reverse=True):
            print('{fk_prefix}{fk_path} ({num}/{count})'.format(count=len(values), **locals()))

    new_indent = indent + '  '
    for child in subtree.children.values():
        print_subtree(child, line_length, new_indent)
