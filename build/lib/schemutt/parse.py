from collections import defaultdict
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


def parse_file_at_path(path):
    parser = make_parser()
    handler = GenericHandler()
    parser.setContentHandler(handler)
    parser.parse(path)
    return handler.tree


def stack_key_path(stack, attr_name=None):
    """Tag.Tag.Tag/Attribute"""
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
