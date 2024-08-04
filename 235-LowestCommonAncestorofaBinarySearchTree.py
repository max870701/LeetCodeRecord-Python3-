# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        val1 = max(p.val, q.val)
        val2 = min(p.val, q.val)
        
        return self.find(root, val1, val2)

    
    # 給定 root 為根節點的 Binary Search Tree，返回含有 val1, val2 的最近公共祖先節點
    def find(self, root, val1, val2):
        if not root: return None
        # 已知 val1 > val2
        # 當前節點太大，去左子樹找
        if root.val > val1:
            return self.find(root.left, val1, val2)
        # 當前節點太小，去右子樹找
        if root.val < val2:
            return self.find(root.right, val1, val2)
        # val1 <= root.val <= val2，則當前節點為 LAC
        return root
    
class Solution1:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Given a root node, p node, q node, return the lowest common ancestor of p, q nodes.
        """
        # Binary Search Tree (BST) where all node values are unique
        if p.val == root.val:
            return p
        elif q.val == root.val:
            return q

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root