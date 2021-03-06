# coding:utf-8
from __future__ import print_function
import argparse
from .main import get_random_emoticon, emoticon_map


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('emo', help='Get an emoticon!')
    args = parser.parse_args()
    try:
        print(get_random_emoticon(args.emo.decode('utf-8'), emoticon_map))
    except IndexError:
        print('Emoticon not found~~')
