from collections import defaultdict


def without_defaultdict():

    sentence = 'The woman and the men are couple.'

    words = sentence.split(' ')

    reg_dict = {}

    for word in words:
        if word in reg_dict:
            reg_dict[word] += 1
        else:
            reg_dict[word] = 1

    print(reg_dict)


def with_defaultdict():
    sentence = 'The woman and the men are couple.'

    words = sentence.split(' ')

    # reg_dict = defaultdict(lambda: 0)
    reg_dict = defaultdict(int)

    for word in words:
        reg_dict[word] += 1
    print(reg_dict)


def with_defaultdict1():
    my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
               (345, 222.66), (678, 300.25), (1234, 35.67)]

    d = defaultdict(list)
    for acct_num, value in my_list:
        d[acct_num].append(value)

    print(d)


def with_defaultdict2():
    name = defaultdict(lambda: "default last name")
    name['Sam'] = 'Yo'
    print(name['Jack'])
    print(name)


if __name__ == '__main__':
    without_defaultdict()
    with_defaultdict()
    with_defaultdict1()
    with_defaultdict2()
