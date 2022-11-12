# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p1 = dummy1 = ListNode(-1)
        p2 = dummy2 = ListNode(-1)
        p = head
        while p is not None:
            # sub-NodeList 1
            if p.val < x:
                p1.next = p
                p1 = p1.next
            # sub-NodeList 2
            else: # p.val >= x
                p2.next = p
                p2 = p2.next
            # To avoid cycle in the ListNode
            tmp = p.next
            p.next = None
            p = tmp
        
        p1.next = dummy2.next
        
        return dummy1.next