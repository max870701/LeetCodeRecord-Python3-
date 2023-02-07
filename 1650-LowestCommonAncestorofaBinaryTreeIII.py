"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        # parent 想成 next 指針，題目變為單鏈表相交問題
        a, b = p, q
        while a != b:
            # a 走一步，如果走到根節點，轉到 q 節點
            if a is None:
                a = q
            else:
                a = a.parent
            # 走一步，如果走到根節點，轉到 p 節點
            if b is None:
                b = p
            else:
                b = b.parent
        return a