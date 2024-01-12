
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

print(nestedListWeightSum([1, [4, [6]]]) == 27)