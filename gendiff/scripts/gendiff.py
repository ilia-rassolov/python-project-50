#!/usr/bin/env python3

from gendiff.parser_args import args
from gendiff.make_diff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.flat import flat


def main():
    # if format not in (flat, stylish):
    #     raise Exception('not correct name formatter')
    diff = generate_diff(args.first_file, args.second_file, format=stylish)
    print(diff)


if __name__ == '__main__':
    main()
