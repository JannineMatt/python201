from collections import deque
import string
import sys
import time
"""
deque
https://docs.python.org/3/library/collections.html#collections.deque
deque O(1) list O(n)
1. deques are a generalization of stacks and queues, They are pronounced “deck” which is short for “double-ended queue”
2. Deques are thread-safe and support memory efficient appends and pops from either side of the deque
3. A deque accepts a maxlen argument which sets the bounds for the deque. Otherwise the deque will grow to an arbitrary size. When a bounded deque is full,
any new items added will cause the same number of items to be popped off the other end.
"""


def get_last(filename, n=5):
    """Return last n lines from file
    Bounded length deques provide functionality similar to the tail filter in Unix:
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        # print("Error opening file: {}".format(filename))
        raise Exception("Error opening file: {}".format(filename))


if __name__ == '__main__':

    d = deque(string.ascii_lowercase)
    for letter in d:
        print(letter)
    d.append('bork')

    print(d)

    d.appendleft('test')
    print(d)

    d.rotate(1)
    print(d)

    for i in range(len(d) - 1):
        d.rotate(1)
        sys.stdout.flush()
        time.sleep(0.2)
        print('\r{}'.format(d), end='')
