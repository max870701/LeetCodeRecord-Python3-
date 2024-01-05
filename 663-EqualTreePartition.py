# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        self.sum_set = set()
        tree_sum = root.val + self.sumTree(root.left) + self.sumTree(root.right)
        if tree_sum % 2 != 0: return False
        # 若有子樹和 tree_sum // 2 在集合中，則可以平分
        return (tree_sum // 2) in self.sum_set

    # 給定 root 為根節點的二叉樹，返回二叉樹所有節點之和
    def sumTree(self, root) -> int:
        if root is None: return 0

        leftSum = self.sumTree(root.left)
        rightSum = self.sumTree(root.right)
        # 後序位置，計算二叉樹所有節點之和，並記錄在 set() 中
        rootSum = leftSum + rightSum + root.val
        self.sum_set.add(rootSum)
        return rootSum