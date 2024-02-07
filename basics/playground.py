import re
import bisect
import itertools
from collections import defaultdict
import heapq
import random


def substitute(s):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

# print(substitute('111221'))
# print(substitute('113221'))
# print(substitute('116221'))
# print(f'{4} + {5} = {4 + 5}')

# print([1,2,3][12,23])

# print([1,2,3])

# print(type("hello"[0]))

fruits = [(0, 'apple'), (1, 'banana'), (2, 'mango')]

# for i, fruit in enumerate(fruits):
#     print(f'{i}: {fruit}')

# dict = {'a': 1, 'b': 2, 'c': 3}
# for tuple in dict.items():
#     print(tuple)

# for tuple in enumerate(dict.keys()):
#     print(tuple)

# print(type([1, 2, 3]))

# print(list(range(1, 10)))

# list_of_lists = [[2, 3], [1, 5], [1, 2]]

# list_of_lists.sort(key=lambda x: x[1])

# print(list_of_lists)

# list_of_lists.sort(key=lambda x: (x[0], -x[1]))
# print(list_of_lists)

# hex_int = 0x23BD
# hex_str = "0x23BD"
# print(str(hex_int))
# print(hex_str)
# for digit in str(hex_int):
#     print(digit)


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
# print(-8//3)


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
    
# print(maximumLength([16,4,1,16,121]))

# print(itertools.pairwise("ABccdedffsasFAS".lower()))

# binary string to integer
# print(int('10000000000000000000000000000010',2))

#count bits, including 0s and 1s
# print(len(str(bin(2147483650))))
# print(str(bin(2147483650)))
# print(2147483650 - 0x7FFFFFFF)

def search(A, t):
    l,r = 0,len(A)-1
    p = A[0]
    while l<r:
        mid = l + (r-l)//2
        m = A[mid]
        # m, t are on the same side of p or not
        if (m < p and t < p):
            m = A[mid]
        else:
            m = float('inf') if t >= p else float('-inf')
        if m < t:
            l = mid + 1
        else:
            r = mid
    
    print(r)
    
    return r if A[r] == t else -1


# print(float('inf'))
# print(0x7FFFFFFF)
# print(float('inf')>0x7FFFFFFF)
# print(0x7FFFFFFE + 1)
# print(0x7FFFFFFE + 2)
# print(0x80000000)
# print(0x80000000 ^ 0xffffffff)

# print(search([12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],0))

def testHeap():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heapq.heapify(nums)
    print(nums)

    nums = [1,3,2,20,45,9,0,-9]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))
    print(heapq.nlargest(3, [-1,-2,-4,-5]))
    print(heapq.nlargest(4, [(100, -2), (100, -1), (300, -3), (400, -4)]))

    arrays = [(100, "a"), (100, "b"), (300, "c"), (400, "d")]
    print(heapq.nlargest(4, arrays, key=lambda x: (x[0], -ord(x[1]))))

    print(heapq.nlargest(4, arrays, key=lambda x: (-x[0], x[1])))

    A = []
    heapq.heappush(A, 1)
    heapq.heappush(A, 0)
    heapq.heappush(A, 9)
    heapq.heappush(A, 8)
    heapq.heappush(A, 2)
    heapq.heappush(A, 3)
    print(A)
    print(A[0]) # Heap top is the smallest element, and access the top using A[0]


def testDictionary():
    data = defaultdict(list)
    data[-1].append(1)
    data[-1].append(2)
    data[-2].append(2)
    data[-3].append(3)
    data[-4].append(4)
    data[5].append(5)
    #sorted(data) will generate a new sorted list of keys.
    print(sorted(data))
    out = [data[i] for i in sorted(data)]
    print(out)


def testRandom():
    print(random.random())
    print(random.random())
    print(random.random())
    print(random.random())

    for _ in range(100):
        print(random.randint(1, 2))

def testJoin():
    print(','.join(['a', 'b', 'c']))


def testList():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(nums))
    print(list(nums).append(10)) # append returns None
    print(list(nums) + [11])

def testSet():
    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(set(nums))
    print(set(nums).add(10)) # add returns None
    print(set(nums) | {11})

    temp = set()
    print(temp.add((1, 'a')))
    print(temp.add((1, 'a')))
    print(temp)

    temp = set()
    # list is not hashable, but tuple is hashable
    print(temp.add([1, 2])) # TypeError: unhashable type: 'list'
    print(temp.add([1, 2])) # TypeError: unhashable type: 'list'

def testFlatList():
    data = [[(0, '8'), ('8', 0), (0, 0, '8')], [(0, '3'), ('3', 1), (0, 0, '3')]]
    flat_list = [item for sublist in data for item in sublist]
    print(flat_list)
    # sum(data, []) is equivalent to the above list comprehension
    sumed = sum(data, [])
    print(sumed)

def testListComprehension():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data = [item for row in matrix for item in row]
    print(data)
    data = [item for row in matrix for item in row if item % 2 == 0]
    print(data)

testFlatList()
testListComprehension()
# testList()
# testRandom()
# testDictionary()

# testHeap()


# testSet()
