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
        # 效率高
        self.val2index = {e:i for i, e in enumerate(inorder)}
        return self.build(preorder, 0 , len(preorder) - 1,
                            inorder, 0, len(inorder) - 1)
    

    def build(self, preorder, preStart, preEnd,
                inorder, inStart, inEnd):
        if preStart > preEnd:
            return None
        
        # root.val 為前序遍歷數組的第一個元素
        root = TreeNode(val=preorder[preStart])
        # root.val 在中序遍歷數組中的索引
        index = self.val2index[root.val]
        # 計算 leftSize 大小
        leftSize = index - inStart

        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                                inorder, inStart, index - 1)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                inorder, index + 1, inEnd)

        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, 0, len(preorder)-1 , inorder, 0, len(inorder)-1)

    # 依照 preorder 和 inorder 構造樹
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd: return None
        
        rootVal = preorder[preStart]
        index = 0

        # 效率較低
        for i in range(inStart, inEnd+1):
            if inorder[i] == rootVal:
                index = i
                break

        leftSize = index - inStart

        root = TreeNode(val=rootVal)
        root.left = self.build(preorder, preStart+1, preStart+leftSize, inorder, inStart, index-1)
        root.right = self.build(preorder, preStart+leftSize+1, preEnd, inorder, index+1, inEnd)

        return root