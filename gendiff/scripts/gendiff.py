#!/usr/bin/env python3


from gendiff.parser import args
from gendiff.make_diff import generate_diff


def main():
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
