# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        定義：輸入節點 root, 然後 root 為根的二叉樹就會被拉平為一條鏈表
        步驟 1: 先利用 flatten(x.left) 和 flatten(x.right) 將 x 的左右子樹拉平
        步驟 2: 將 x 的右子樹接到左子樹下方，然後將整個左子樹作為右子樹
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # base case
        if root is None:
            return
        
        #利用定義拉平左右子樹
        self.flatten(root.left)
        self.flatten(root.right)

        # 1.左右子樹已經被拉平成一條鏈表
        flatten_left = root.left
        flatten_right = root.right

        # 2.左子樹作為右子樹
        root.left = None
        root.right = flatten_left

        # 3.將原先的右子樹接到當前右子樹的末端
        p = root # root 現在為新的 root, 僅有新接上的右節點（舊的左節點）
        while p.right:
            p = p.right
        # 當 p.right is None 時跳出 while, 此時接上舊的右節點
        p.right = flatten_right