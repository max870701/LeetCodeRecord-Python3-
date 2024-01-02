"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # parent 想成 next 指針，題目變為單鏈表相交問題
        p1, p2 = p, q
        while p1 != p2:
            # p1 走一步，如果走到根節點，轉到 q 節點
            if p1 is None:
                p1 = q
            else:
                p1 = p1.parent
            # p2 走一步，如果走到根節點，轉到 p 節點
            if p2 is None:
                p2 = p
            else:
                p2 = p2.parent
        
        return p1