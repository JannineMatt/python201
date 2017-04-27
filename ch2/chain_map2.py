import argparse
import os
from collections import ChainMap

"""
using ChainMap, we can check user input arg and default arg
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='username')
    parser.add_argument('-p', '--password', help='password')
    return parser.parse_args()


def main():
    app_defaults = {'username': 'admin', 'password': 'admin'}
    args = get_args()
    # print(vars(args))
    command_line_args = {key: value for key, value in vars(args).items() if value}
    chain = ChainMap(command_line_args, app_defaults)
    print(chain)
    print(chain['username'])


if __name__ == '__main__':
    main()
