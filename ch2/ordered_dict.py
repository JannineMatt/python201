from collections import OrderedDict

# dict is not ordered
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(d)

new_d = OrderedDict(sorted(d.items()))
print(new_d)
