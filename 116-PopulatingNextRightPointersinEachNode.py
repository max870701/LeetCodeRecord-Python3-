"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #問題抽象為遍歷三叉樹相鄰節點
        if root is None: return None
        self.traverse(root.left, root.right)
        return root

    # 遍歷三叉樹
    def traverse(self, node1, node2):
        if (node1 is None) or (node2 is None):
            return None
        #前序
        node1.next = node2
        
        self.traverse(node1.left, node1.right)
        self.traverse(node1.right, node2.left)
        self.traverse(node2.left, node2.right)