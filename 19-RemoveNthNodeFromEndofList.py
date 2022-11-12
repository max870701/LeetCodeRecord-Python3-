# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1, head)
        x = self.findFromEnd(dummy, n+1)
        x.next = x.next.next
        
        return dummy.next
    
    def findFromEnd(self, head, k):
        p1 = p2 = head
        for i in range(k):
            p1 = p1.next
        while p1 is not None:
            p1, p2 = p1.next, p2.next
        return p2