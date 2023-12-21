import re


def substitute(s):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

print(substitute('111221'))
print(substitute('113221'))
print(substitute('116221'))

print(f'{4} + {5} = {4 + 5}')


print(type("hello"[0]))

fruits = [(0, 'apple'), (1, 'banana'), (2, 'mango')]

for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')

dict = {'a': 1, 'b': 2, 'c': 3}
for tuple in dict.items():
    print(tuple)

for tuple in enumerate(dict.keys()):
    print(tuple)

print(type([1, 2, 3]))

print(list(range(1, 10)))

list_of_lists = [[2, 3], [1, 5], [1, 2]]

list_of_lists.sort(key=lambda x: x[1])

print(list_of_lists)

list_of_lists.sort(key=lambda x: (x[0], -x[1]))
print(list_of_lists)

hex_int = 0x23BD
hex_str = "0x23BD"
print(str(hex_int))
print(hex_str)
for digit in str(hex_int):
    print(digit)


