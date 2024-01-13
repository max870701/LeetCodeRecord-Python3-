# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定 root 和 subRoot 為根節點的兩棵樹，返回 subRoot 是否為 root 的子樹。
    # 節點內要做的事
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        
        if self.isSametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # 給定 tree1 和 tree2 為根節點的兩顆二叉樹，判斷是否相同
    def isSametree(self, tree1, tree2):
        if tree1 is None and tree2 is None:return True
        if tree1 is None or tree2 is None: return False
        if tree1.val != tree2.val: return False
        
        return self.isSametree(tree1.left, tree2.left) and self.isSametree(tree1.right, tree2.right)
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    # 給定 root 為根節點的二叉樹，判斷 subRoot 為根節點的二叉樹是否為子樹
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # 給定兩個 root1, root2，判斷是否為相同一棵樹
    def isSameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        if root1.val != root2.val:
            return False

        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)