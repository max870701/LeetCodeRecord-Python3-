# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    # 給定 root 為根節點的二叉樹，返回最大寬度
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 層序遍歷
        if root is None: return 0
        q = Queue()
        q.put((root, 1))
        maxWidth = 0
        while not q.empty():
            size = q.qsize()
            start, end = 0, 0
            for i in range(size):
                cur_node, cur_index = q.get()
                
                if i == 0:
                    start = cur_index
                if i == size - 1:
                    end = cur_index
                if cur_node.left is not None:
                    q.put((cur_node.left, 2 * cur_index))
                if cur_node.right is not None:
                    q.put((cur_node.right, 2 * cur_index + 1))

            maxWidth = max(maxWidth, end - start + 1)

        return maxWidth