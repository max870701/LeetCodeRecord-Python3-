# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.setCamera(root, False)
        return self.res
    
    # 給定 root 為根節點的二叉樹，用最優策略放置camera，返回root的狀態
    # -1: root 為空
    #  0: root uncovered
    #  1: root covered
    #  2: root 放上 camera
    def setCamera(self, root: Optional[TreeNode], hasParent: bool) -> int:
        if root is None: return -1
        left_status = self.setCamera(root.left, True)
        right_status = self.setCamera(root.right ,True)
        # 後序位置：判斷左右子樹狀態，決定 root 的返回狀態
        # root 為葉子節點
        if left_status == -1 and right_status == -1:
            if hasParent:
                return 0
            else:
                self.res += 1
                return 2
        # 左右子樹之一 uncovered
        if left_status == 0 or right_status == 0:
            self.res += 1
            return 2
        # 左右子樹其中一個有設置 camera
        if left_status == 2 or right_status == 2:
            return 1
        # 左右子樹(若有)都被 covered
        # if (left_status == 1 and right_status == 1) or (left_status == -1 and right_status == 1) or (left_status == 1 and right_status == -1)
        if hasParent:
            return 0
        else:
            self.res += 1
            return 2