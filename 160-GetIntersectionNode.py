# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from unittest.mock import NonCallableMagicMock


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Time complexity is O(M+N)
        # Space complexity is O(M), where (M > N)
        if headA == headB:return headA
        
        tmp = set() #hash set
        
        while headA:
            tmp.add(headA)
            headA = headA.next
            
        if len(tmp):
            while headB:
                if headB in tmp:return headB
                headB = headB.next
        return None
    

    def getIntersectionNode1(self, headA, headB):
        # Concept: len(headA) + len(headB) == len(headB) + len(headA)
        # Time complexity is O(M+N)
        # Space complexity is O(1)
        if headA is None or headB is None:
            return None

        pA = headA
        pB = headB
        
        while (pA != pB):
            if pA is None: # switch the path of pointer to another ListNode
                pA = headB
            else:
                pA = pA.next

            if pB is None: # switch the path
                pB = headA
            else:
                pB = pB.next
        
        return pA