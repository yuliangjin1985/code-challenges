## Basic usages
### sorting
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
