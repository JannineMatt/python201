import argparse


def store():
    print('come from store')


def get_args():

    parser = argparse.ArgumentParser(
        description='simple argument paser',
    )

    # requirement args
    # about action, please check
    # [argparse](https://docs.python.org/dev/library/argparse.html#action)
    parser.add_argument('-x', action='store', required=True,
                        help='help text for option X')
    # optional args
    parser.add_argument('-y', action='store', type=bool, default=False,
                        help='help text for option Y')
    parser.add_argument('-z', action='store', type=int,
                        help='help text for option Z')
    parser.add_argument('-o', '--output', type=str,
                        help='help text for option O')
    print(parser.parse_args())


if __name__ == '__main__':
    get_args()

"""
use case

$python args2.py -h
usage: args2.py [-h] -x X [-y Y] [-z Z]

simple argument paser

optional arguments:
  -h, --help  show this help message and exit
  -x X        help text for option X
  -y Y        help text for option Y
  -z Z        help text for option Z

$ python args2.py                                                                                                                    Thu 27 Apr 2017 12:04:46 AM CST
usage: args2.py [-h] -x X [-y Y] [-z Z]
args2.py: error: the following arguments are required: -

$ python args2.py -x 1
Namespace(x='1', y=False, z=None)

$ python args2.py -x 1 -y True
Namespace(x='1', y=True, z=None)

$ python args2.py -x 1 -y 1 -z 0
Namespace(x='1', y=True, z=0)
"""
