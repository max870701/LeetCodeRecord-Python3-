# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.nodes = []
        self.traverse(root, 0, 0)
        self.nodes.sort(key=lambda x: (x[2], x[1], x[0]))

        res = []
        prev_col = -1001
        for node in self.nodes:
            cur_col = node[2]
            if prev_col != cur_col:
                res.append([])
                prev_col = cur_col
            res[-1].append(node[0])

        return res
    
    def traverse(self, root, row, col):
        if root is None: return
        self.nodes.append((root.val, row, col))
        self.traverse(root.left, row + 1, col - 1)
        self.traverse(root.right, row + 1, col + 1)