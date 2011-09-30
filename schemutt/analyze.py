def all_attr_values(tree):
    """Yield (node, attr_name, attr_values) for each attribute on each node"""
    stack = [tree]
    while stack:
        node = stack.pop()
        for attr_name, attr_values in node.attr_values():
            yield (node, attr_name, attr_values)
        for child_node in node.children.values():
            stack.append(child_node)


def find_foreign_keys(tree):
    for node, attr_name, attr_values in all_attr_values(tree):
        for check_node, check_attr_name, check_attr_values in all_attr_values(tree):
            if node != check_node and len(attr_values) > 2 and len(check_attr_values) > 2:
                sub_key_path = check_node.key_path + '/' + check_attr_name
                common = attr_values & check_attr_values
                if len(common) > len(attr_values) * 0.1:
                    node.add_foreign_key(attr_name, (len(common), sub_key_path))
