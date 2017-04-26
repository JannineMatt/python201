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
    # using exclusive group, only one of this can assign
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-y', action='store', type=bool, default=False,
                       help='help text for option Y')
    group.add_argument('-z', action='store', type=int,
                       help='help text for option Z')
    parser.add_argument('-o', '--output', type=str,
                        help='help text for option O')
    print(parser.parse_args())


if __name__ == '__main__':
    get_args()

"""
use case

$python args3.py -h
usage: args3.py [-h] -x X [-y Y | -z Z] [-o OUTPUT]

simple argument paser

optional arguments:
  -h, --help            show this help message and exit
  -x X                  help text for option X
  -y Y                  help text for option Y
  -z Z                  help text for option Z
  -o OUTPUT, --output OUTPUT
                        help text for option O

$ python args3.py                                                                                                                    Thu 27 Apr 2017 12:04:46 AM CST
usage: args3.py [-h] -x X [-y Y] [-z Z]
args3.py: error: the following arguments are required: -

$ python args3.py -x 1
Namespace(output=None, x='1', y=False, z=None)

$ python args3.py -x 1 -y True
Namespace(output=None, x='1', y=True, z=None)


$ python args3.py -x 1 -y 1 -z 0
usage: args3.py [-h] -x X [-y Y | -z Z] [-o OUTPUT]
args3.py: error: argument -z: not allowed with argument -y
"""
