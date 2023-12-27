# Basic usages

## 435 Non-overlapping intervals

```python
    #less is more
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            first, second = intervals[i]
            if first >= end:
                end = second
                count += 1
        return len(intervals) - count

```

```python
# intervals: List[List[int]], first sort based on the first element on assending order, if equal, then sort on second element by descending order
intervals.sort(key=lambda x: (x[0], -x[1]))
```

## 100 Same tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

```

## 297. Serialize and deserialize binary tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def ser(node):
            if node:
                strs.append(str(node.val))
                ser(node.left)
                ser(node.right)
            else:
                strs.append('#')
        strs = []
        ser(root)
        return ' '.join(strs)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def des():
            val = next(strs)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = des()
            node.right = des()
            return node
        strs = iter(data.split())
        return des()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root)
```

## 235 Lowest common ancestor of a binary search tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

```python
def lowestCommonAncestor(self, root, p, q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = (root.left, root.right)[p.val > root.val] # works like `? :` in java
    return root
```

## 208 Implement Trie/Prefix Tree

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

`Trie()` Initializes the trie object.
`void insert(String word)` Inserts the string word into the trie.
`boolean search(String word)` Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
`boolean startsWith(String prefix)` Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

```python
class Trie:

    def __init__(self):
        self.dict = {}
        

    # Each letter in the word is mapped with a dict, and if the dict of the last letter contains a key *, then it's a word
    def insert(self, word: str) -> None:
        cur = self.dict
        for letter in word:
            if letter not in cur:
                cur[letter] = {} 
            cur = cur[letter]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.dict
        for l in word:
            if l not in cur:
                return False
            cur = cur[l]
        return '*' in cur
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.dict
        for l in prefix:
            if l not in cur:
                return False
            cur = cur[l]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix
```

### 845 Longest mountain in an array

```python
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        up, down = [0] * n, [0] * n
        for i in range(1, n):
            if arr[i] > arr[i-1]: up[i] = up[i-1] + 1
        for i in range(n-1)[::-1]:
            if arr[i] > arr[i+1]: down[i] = down[i+1] + 1
        ret = 0
        for i in range(1, n - 1):
            if up[i] > 0 and down[i] > 0:
                ret = max(ret, up[i] + down[i] + 1)
        return ret
```

### 152 Max Product Subarray

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

>Because if there is such a sub array, it has to be starting with one item (prefix product, A in the below code) or ending with one item (suffix product, B in the below code), so we enumerate for all these possibilities. If current item is 0, the subarray starts, ends with, or contains this item will have product as 0. For next item, it contributes 1 instead of 0. That's why `A[i] *= A[i-1] or 1` is so elegantly coded.

```python
class Solution:
    def maxProduct(self, A: List[int]) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1 #Inplace updating the initial list with pre product value
            B[i] *= B[i-1] or 1
        return max(max(A), max(B))
```

### 628 Maximum product of three numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = heapq.nsmallest(3, nums) # Time complexity: n * O(ln3)
        b = heapq.nlargest(3, nums)
        return max(a[0]*a[1]*b[0], b[0]*b[1]*b[2])
```

### 32 Longest valid parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses *substring*.

**Solution**:
> Use a stack to store the index of the '(' or ')', and when there is a pair of valid parenthese, pop the top element, eventually only invalid indexes are in the stack. And substring between two invalid indexes is a valid parenthese substring. Put index `-1` and `n` as the boundaries.

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1) # Add lower boundary
        for i in range(len(s)):
            if s[i] == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        
        stack.append(len(s)) # Add upper boundary
        ret = 0
        for i in range(1,len(stack)):
            ret = max(ret, stack[i] - stack[i-1] - 1)

        return ret
```
