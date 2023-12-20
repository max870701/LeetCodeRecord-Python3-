# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 給定 root 為根節點的二叉樹和 head 為初始節點的鏈表，返回是否存在 subPath
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Base case 
        if head is None: return True
        if root is None: return False
        # 若鏈表頭節點的值與以root為根節點的二叉樹的值對上
        if head.val == root.val:
            # 判斷是否能填入 root 以下的路徑
            if self.check(head, root):
                return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    
    def check(self, head, node):
        # Base case
        if head is None: return True
        if node is None: return False

        if head.val == node.val:
            return self.check(head.next, node.left) or self.check(head.next, node.right)
        
        return False