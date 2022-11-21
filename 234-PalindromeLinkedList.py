# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.left = head
        return self.traverse(head)
    
    
    def traverse(self, right):
        if right is None:
            return True
        # Recursion
        global res
        res = self.traverse(right.next)
        # From the end
        # boolean operation
        res = (res) and (right.val == self.left.val)
        self.left = self.left.next
        return res