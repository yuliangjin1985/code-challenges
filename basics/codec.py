# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left 
        self.right = right

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


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, None), None)
    print(Codec().serialize(root))
