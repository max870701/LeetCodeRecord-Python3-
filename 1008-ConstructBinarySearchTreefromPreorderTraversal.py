# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.buildBST(preorder, 0, len(preorder)-1)
    
    # 給定 preorder 數組和 start, end 範圍，構造出BST
    def buildBST(self, preorder, start, end):
        if start > end: return

        root = TreeNode(val=preorder[start])
        index = start + 1

        while index <= end and preorder[index] < root.val:
            index += 1

        root.left = self.buildBST(preorder, start+1, index - 1)
        root.right = self.buildBST(preorder, index, end)

        return root