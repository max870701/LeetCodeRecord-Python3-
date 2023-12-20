# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self.tmp = []
        self.curSum = 0
        self.target = targetSum
        self.traverse(root)
        return self.ans

    # 遍歷以 root 為根節點的二叉樹，到達葉子節點時檢查是否與 targetSum 相同，若相同，則記錄路徑上的所有節點值。
    def traverse(self, root):
        if root is None:
            return
        # pre order
        self.curSum += root.val
        self.tmp.append(root.val)
        if root.left is None and root.right is None:
            if self.curSum == self.target:
                self.ans.append(self.tmp[:]) # 注意引用問題
        self.traverse(root.left)
        # in order
        self.traverse(root.right)
        # post order
        self.curSum -= root.val
        self.tmp.pop()