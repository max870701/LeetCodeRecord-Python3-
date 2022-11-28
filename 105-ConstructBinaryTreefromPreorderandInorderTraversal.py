# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        根據前序和中序遍歷構建二叉樹
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.val2index = { inorder[i]: i for i in range(len(inorder))}
        return self.build(preorder, 0 , len(preorder) - 1,
                            inorder, 0, len(inorder) - 1)
    

    def build(self, preorder, preStart, preEnd,
                inorder, inStart, inEnd):
        if preStart > preEnd:
            return None
        
        # root 為前序遍歷數組的第一個元素
        rootVal = preorder[preStart]
        # root val 在中序遍歷數組中的索引
        #index = inorder.index(rootVal, inStart, inEnd+1)
        index = self.val2index[rootVal]

        root = TreeNode(val=rootVal)

        leftSize = index - inStart
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                                inorder, inStart, index - 1)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                inorder, index + 1, inEnd)

        return root