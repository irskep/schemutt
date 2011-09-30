import argparse

from schemutt.analyze import find_foreign_keys
from schemutt.out import print_subtree
from schemutt.parse import parse_file_at_path


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


def main():
    args = make_arg_parser().parse_args()
    for path in args.path:
        print(path)
        tree = parse_file_at_path(path)
        if args.find_foreign_keys:
            find_foreign_keys(tree)
        print_subtree(tree, args.line_length)


if __name__ == '__main__':
    main()
