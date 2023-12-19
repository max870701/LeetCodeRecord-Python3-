"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 分解問題的思路
class Solution:
    # 返回 root 為根節點的多叉樹的最大深度
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        self.subTreeDepth = 0
        for child in root.children:
            self.subTreeDepth = max(self.subTreeDepth, self.maxDepth(child))
        return self.subTreeDepth + 1

# 遍歷的思路
class Solution2:
    def maxDepth(self, root: 'Node') -> int:
        self.ans = 0
        self.d = 0
        self.traverse(root)
        return self.ans

    # 遍歷以 root 為根節點的多叉樹，並維護當前深度與最大深度
    def traverse(self, root):
        if root is None: return
        self.d += 1
        self.ans = max(self.ans, self.d)
        for child in root.children:
            self.traverse(child)
        self.d -= 1