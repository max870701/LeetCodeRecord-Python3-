# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.arr = [0 for _ in range(10)]
        self.cnt = 0
        self.traverse(root)
        return self.cnt

    def traverse(self, root):
        if root is None: return
        
        if root.left is None and root.right is None:
            self.arr[root.val] += 1
            if self.check(): 
                self.cnt += 1
            self.arr[root.val] -= 1
            return

        self.arr[root.val] += 1
        self.traverse(root.left)
        self.traverse(root.right)
        self.arr[root.val] -= 1

    def check(self):
        cond = False
        for i in range(1, 10):
            cnt = self.arr[i]
            # if cnt % 2 == 0: continue
            if not cond and cnt % 2 == 1:
                cond = True
            elif cnt % 2 == 1:
                return False
        return True