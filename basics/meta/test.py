
def nestedListWeightSum(nestedList):
    def helper(nestedList, depth):
        out = 0
        for item in nestedList:
            if isinstance(item, list):
                out += helper(item, depth + 1)
            else:
                out += item * depth
        return out
    
    return helper(nestedList, 1)

# tests

# print(nestedListWeightSum([1, [4, [6]]]) == 27)
arr1 = [[1,4], [1,3], [0,5], [4,5], [0,2]]
arr2 = [[1,4], [1,3], [0,5], [4,5], [0,2]]
arr3 = [[1,4], [1,3], [0,5], [4,5], [0,2]]
arr1.sort()
arr2.sort(key=lambda x: (x[0],x[1]))
arr3.sort(key=lambda x: x[0])
print(arr1 == arr2)
print(arr2 != arr3)
print(arr3)