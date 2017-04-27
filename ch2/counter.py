from collections import Counter


counter = Counter('superfluous')
# Counter will calculate each character how many time show up
# return a dict {character:times,}
print(counter)
print(counter['u'])
# list all elements
print(list(counter.elements()))
print(counter.most_common())
print(counter.most_common(2))
print(counter.most_common(1))
