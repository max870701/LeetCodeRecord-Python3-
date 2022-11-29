# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        給中序和後序遍歷，構建二叉樹
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.val2index = {inorder[i]: i for i in range(len(inorder))}
        return self.build(inorder, 0, len(inorder) - 1,
                            postorder, 0, len(postorder) - 1)

    def build(self, inorder, inStart, inEnd,
                    postorder, postStart, postEnd):
        """
        給 inorder[inStart:inEnd] 和 postorder[postStart:postEnd]
        構造二叉樹，並返回二叉樹的根節點
        """
        if inStart > inEnd:
            return None

        rootVal = postorder[postEnd]
        index = self.val2index[rootVal]

        leftSize = index - inStart

        root = TreeNode(val=rootVal)
        root.left = self.build(inorder, inStart, index - 1,
                                postorder, postStart, postStart + leftSize - 1)
        root.right = self.build(inorder, index + 1, inEnd,
                                postorder, postStart + leftSize, postEnd - 1)

        return root