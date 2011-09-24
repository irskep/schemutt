import argparse
from collections import defaultdict
import re
import sys
import weakref
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


def stack_key_path(stack, attr_name=None):
    s = '.'.join([e.name for e in stack])
    if attr_name:
        s += '/' + attr_name
    return s


class Element:
    def __init__(self, name, stack_below):
        self.name = name
        self.attributes = defaultdict(set)
        self.foreign_keys = defaultdict(list)
        self.children = {}
        self.key_path = stack_key_path(stack_below + [self])

    def add_attr_value(self, attr_name, attr_value):
        self.attributes[attr_name].add(attr_value)

    def add_foreign_key(self, attr_name, fk_value):
        self.foreign_keys[attr_name].append(fk_value)

    def attr_values(self):
        return self.attributes.items()

    def foreign_keys(self, attr_name):
        return self.foreign_keys[attr_name]


class GenericHandler(ContentHandler):

    def __init__(self):
        self.tree = None
        self.stack = []

    def startElement(self, name, attributes):
        if self.stack:
            last_elem = self.stack[-1]
            last_elem.children.setdefault(name, Element(name, self.stack))
            my_elem = last_elem.children[name]
        else:
            my_elem = Element(name, self.stack)
            self.tree = my_elem

        for attr_name in attributes.getNames():
            attr_value = attributes.getValue(attr_name)
            my_elem.add_attr_value(attr_name, attr_value)

        self.stack.append(my_elem)

    def endElement(self, name):
        self.stack.pop()


def parse_file_at_path(path):
    parser = make_parser()
    handler = GenericHandler()
    parser.setContentHandler(handler)
    parser.parse(path)
    return handler.tree


def all_attr_values(tree):
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


def values_within_line_length(values, line_length):
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


def make_arg_parser():
    parser = argparse.ArgumentParser(description='Attempt to derive and display'
                                     ' a basic outline of the schema of an XML'
                                     ' document')
    parser.add_argument('path', type=str, nargs='+', help='Path to an XML document')
    parser.add_argument('--find-foreign-keys', dest='find_foreign_keys',
                        action='store_true', default=False,
                        help='Attempt to determine relationships between'
                        ' attribute values')
    parser.add_argument('--line-length', type=int, dest='line_length', default=80,
                        help='Maximum number of characters in a line (use more'
                        ' to see more attribute examples)')
    return parser


if __name__ == '__main__':
    args = make_arg_parser().parse_args()
    for path in args.path:
        print(path)
        tree = parse_file_at_path(path)
        if args.find_foreign_keys:
            find_foreign_keys(tree)
        print_subtree(tree, args.line_length)
