# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
            if pA is None: # pA 指針到底後指回 headB
                pA = headB
            else:
                pA = pA.next

            if pB is None: # pB 指針到底後指回 headA
                pB = headA
            else:
                pB = pB.next
        # 兩者相等時，即為接點
        return pA
    

class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None: return None

        p1 = headA
        p2 = headB
        diff = 0
        while p1:
            p1 = p1.next
            diff += 1
        while p2:
            p2 = p2.next
            diff -= 1
        
        if diff > 0:
            p1 = headA
            p2 = headB
        else:
            p1 = headB
            p2 = headA
        diff = abs(diff)
        while diff:
            p1 = p1.next
            diff -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1