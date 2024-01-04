# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.findBST(root)
        return self.res

    # 給定 root 為根節點的二叉樹，若非BST，則返回 None
    # 若是 BST，返回BST的 (最小值, 最大值, 節點個數)
    def findBST(self, root):
        if root is None:
            return (float('inf'), float('-inf'), 0)
        
        left = self.findBST(root.left)
        right = self.findBST(root.right)

        # 若左或右子樹存在但非 BST，返回 None
        if left is None or right is None:
            return None

        left_min, left_max, left_node_cnt = left
        right_min, right_max, right_node_cnt = right

        # 判斷當前 root 是否符合 BST 條件
        if root.val > left_max and root.val < right_min:
            root_min = min(left_min, root.val)  # 若左子樹不存在，則 root.val 為最小值
            root_max = max(right_max, root.val) # 若右子樹不存在，則 root.val 為最大值
            root_node_cnt = left_node_cnt + right_node_cnt + 1
            self.res = max(self.res, root_node_cnt)
            return (root_min, root_max, root_node_cnt)
        
        # 當前 root 為根節點的二叉樹非BST
        return None