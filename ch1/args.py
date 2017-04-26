import argparse


def get_args():

    parser = argparse.ArgumentParser(
        description='simple argument paser',
    )
    return parser.parse_args()


if __name__ == '__main__':
    # call with
    # python args.py -h
    get_args()
