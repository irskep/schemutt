import argparse
from pprint import pprint
import re
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class GenericHandler(ContentHandler):

    def __init__(self):
        # {
        #  'name': blah,
        #  'attributes': {'name': blah, 'values': set()},
        #  'children': {name1: {recurse}, name2... },
        # }
        self.tree = None
        # [dict, dict dict...]
        self.stack = []

    def startElement(self, name, attributes):
        if self.stack:
            last_dict = self.stack[-1]
            last_dict['children'].setdefault(name, {'name': name,
                                                    'attributes': {},
                                                    'children': {}})
            my_dict = last_dict['children'][name]
        else:
            my_dict = {'name': name, 'attributes': {}, 'children': {}}
            self.tree = my_dict
        for attr in attributes.getNames():
            my_dict['attributes'].setdefault(attr, set())
            my_dict['attributes'][attr].add(attributes.getValue(attr))

        self.stack.append(my_dict)

    def endElement(self, name):
        self.stack.pop()


def parse_file_at_path(path):
    parser = make_parser()
    handler = GenericHandler()
    parser.setContentHandler(handler)
    parser.parse(path)
    return handler.tree


def print_subtree(subtree, line_length, indent=''):
    print('{0}<{1}>'.format(indent, subtree['name']))

    for attr, values in subtree['attributes'].items():
        prefix = '{0}  {1} = '.format(indent, attr)

        ex_values = {values.pop()}

        # limit line length
        if values:
            next_values = ex_values | {values.pop()}
            while next_values and len(prefix) + len(repr(next_values)) < line_length:
                ex_values = next_values
                if values:
                    next_values = ex_values | {values.pop()}
                else:
                    next_values = None

        print('{0}{1}'.format(prefix, ex_values))

    new_indent = indent + '  '
    for child in subtree['children'].values():
        print_subtree(child, line_length, new_indent)


def make_arg_parser():
    parser = argparse.ArgumentParser(description='Attempt to derive and display'
                                     ' a basic outline of the schema of an XML'
                                     ' document')
    parser.add_argument('path', type=str, nargs='+', help='Path to an XML document')
    parser.add_argument('--find-foreign-keys', type=bool,
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
        print_subtree(parse_file_at_path(path), args.line_length)
