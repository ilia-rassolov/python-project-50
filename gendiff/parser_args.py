import argparse
import pathlib


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=pathlib.Path)
parser.add_argument('second_file', type=pathlib.Path)
parser.add_argument('-f', '--format', help='set format of output', default='stylish')

args = parser.parse_args()
