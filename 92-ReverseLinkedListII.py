# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # Base case
        if left == 1:
            return self.reverseN(head, right)
        # Move into the start point of the reverse to trigger the base case
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

    def reverseN(self, head, n):
        global successor
        # Count the nth ListNode
        if n == 1:
            # Record the (n+1)th ListNode
            successor = head.next
            return head
        # Recursively reverse the rest of n-1 ListNode
        last =self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = successor
        return last
        