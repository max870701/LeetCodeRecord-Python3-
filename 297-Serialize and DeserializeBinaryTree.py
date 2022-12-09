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
        self.vals = []
        self.preorder(root)
        return ",".join(self.vals)

    def preorder(self, node):
        if not node:
            self.vals.append("#")
        else:
            self.vals.append(str(node.val))
            self.preorder(node.left)
            self.preorder(node.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.vals = data.split(",")
        return self.build()

    
    def build(self):
        if self.vals:
            val = self.vals.pop(0)
            if val == "#": return None

            root = TreeNode(int(val))
            root.left = self.build()
            root.right = self.build()
            return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))