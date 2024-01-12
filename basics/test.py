import re
import bisect
import itertools
from collections import defaultdict


def substitute(s):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

print(substitute('111221'))
print(substitute('113221'))
print(substitute('116221'))
print(f'{4} + {5} = {4 + 5}')

# print([1,2,3][12,23])

print([1,2,3])

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


def longestValidParentheses(s: str) -> int:
    stack = []
    stack.append(-1)
    for i in range(len(s)):
        if s[i] == ')' and stack and stack[-1] != -1 and s[stack[-1]] == '(':
            stack.pop()
        else:
            stack.append(i)
    
    stack.append(len(s))
    ret = 0
    for i in range(1,len(stack)):
        ret = max(ret, stack[i] - stack[i-1] - 1)

    return ret

# print(longestValidParentheses(")()(((())))("))


# print(bisect.bisect([1,2,3,3,5,6,7,8,9], 3))
# print(bisect.bisect_left([1,2,3,3,5,6,7,8,9], 3))

# print(bisect.bisect([1,2,3,3,5,6,7,8,9], 40))
print(-8//3)


def maximumLength(nums: list[int]) -> int:
        counter = defaultdict(int)
        out = 1
        for num in nums:
            counter[num] += 1
        
        for k,v in counter.items():
            if v == 1:
                out = max(out, 1)
            else:
                b = v
                next = b * b
                temp = 2
                while next in counter and counter[next] > 1:
                    temp += 2
                    next *= next
                if next in counter:
                    temp += 1
                else:
                    temp = 0
                out = max(out, temp)
                    
        return out
    
print(maximumLength([16,4,1,16,121]))

# print(itertools.pairwise("ABccdedffsasFAS".lower()))

# binary string to integer
print(int('10000000000000000000000000000010',2))

#count bits, including 0s and 1s
print(len(str(bin(2147483650))))
print(str(bin(2147483650)))
print(2147483650 - 0x7FFFFFFF)

