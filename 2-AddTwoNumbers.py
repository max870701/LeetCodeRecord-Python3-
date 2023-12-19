# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, cur = None, None
        carry = 0
        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            val = s % 10
            carry = s // 10
            
            if ans is None:
                ans = ListNode(val=val)
                cur = ans
            else:
                cur.next = ListNode(val=val)
                cur = cur.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if carry == 1:
            cur.next = ListNode(val=1)
        
        return ans