# Binary tree

Traversals: preorder, inorder, postorder, for iterative solution, all could use a stack structure. For preorder.

## Preorder traversal

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list, stack = [], []
        node = root
        while node or stack:
            while node:
                list.append(node.val) # Visite node
                stack.append(node)
                node = node.left
            node = stack.pop().right
        return list
```

## Inorder traversal

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list, stack = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            list.append(node.val)
            node = node.right
        return list
```

## 145 Binary Tree Postorder Traversal

For postorder traversal, each valid node has to be pushed to and polled twice to the stack, the first time was with flag `visited` as `False`, the seond is with this flas as `True` when both of its children were pushed to the stack.

The inorder traversal is basically with order `left -> right -> parent`, but the order being pushed should be the opposite: `parent -> right -> left`, so the left will be popped first.

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list, stack, node = [], [], root
        if not root:
            return list
        stack.append((root, False))
        while stack:
            node, visited = stack.pop()
            if visited:
                list.append(node.val)
            else:
                stack.append((node, True))
                if node.right: stack.append((node.right, False))
                if node.left: stack.append((node.left, False))

        return list

```
