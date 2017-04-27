from collections import namedtuple

People = namedtuple('People', ['id', 'name'])
Jack = People(id=1, name='Jack')
print(Jack)
print(Jack.id)

# namedtuple also keep tuple way
# but not orderly
man_id, man_name = Jack
print(man_id, man_name)

Mia = {'id': 2, 'name': 'Mia'}
Student = namedtuple('People', Mia.keys())
Mia = Student(**Mia)
print(Mia)
