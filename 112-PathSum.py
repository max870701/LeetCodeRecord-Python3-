# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found = False
        self.curSum = 0
        self.target = targetSum

        self.traverse(root)

        return self.found
    

    def traverse(self, root):
        # Base case
        if root is None or self.found:
            return
        # 進入 node
        self.curSum += root.val
        # 判斷是否為 leaf node
        if root.left is None and root.right is None:
            if self.curSum == self.target:
                self.found = True

        # 遍歷左右子樹
        self.traverse(root.left)
        self.traverse(root.right)
        # 維護 curSum
        self.curSum -= root.val

        return self.curSum
    

class Solution2:
    # 給定 root 為根節點的二叉樹，判斷路徑和是否為 targetSum
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return root.val == targetSum
        # 穿透性：若左側為 True 則直接返回 True，右側不會再進行判斷
        return (self.hasPathSum(root.left, targetSum - root.val)) or (self.hasPathSum(root.right, targetSum - root.val))