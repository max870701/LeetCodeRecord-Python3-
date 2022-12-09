# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.val2index = {postorder[i]: i for i in range(len(postorder))}
        return self.build(preorder, 0, len(preorder) - 1,
                            postorder, 0, len(postorder) - 1)

    def build(self, preorder, preStart, preEnd,
                    postorder, postStart, postEnd):
        if preStart > preEnd:
            return None

        if preStart == preEnd:
            return TreeNode(val=preorder[preStart])

        rootVal = preorder[preStart]
        leftRootVal = preorder[preStart + 1]
        index = self.val2index[leftRootVal]

        leftSize = index - postStart + 1

        root = TreeNode(val=rootVal)
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                                postorder, postStart, index)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                postorder, index + 1, postEnd - 1)

        return root