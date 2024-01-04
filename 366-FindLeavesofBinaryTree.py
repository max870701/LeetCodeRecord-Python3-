# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.maxDepth(root)
        return self.res

    # 給定 root 為根節點的二叉樹，返回最大高度
    def maxDepth(self, root):
        if root is None: return 0

        left_h = self.maxDepth(root.left)
        right_h = self.maxDepth(root.right)
        h = max(left_h, right_h) + 1
        
        # 後序位置(畫圖理解節點進出順序)
        if len(self.res) <= h-1:
            self.res.append([])
        self.res[h-1].append(root.val)

        return h