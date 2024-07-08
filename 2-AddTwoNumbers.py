# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = dummy = ListNode()
        p1 = l1
        p2 = l2
        carry = 0 # 進位

        while p1 or p2 or carry:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            val = p1_val + p2_val + carry
            carry = val // 10
            val %= 10

            p.next = ListNode(val=val)
            p = p.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return dummy.next

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.convertToList(self.convertToNumber(l1) + self.convertToNumber(l2))
    
    def convertToList(self, num):
        multi = 10
        p = dummy = ListNode()
        if num == 0: return dummy

        while num > 0:
            cur_val = num % multi
            num //= multi
            p.next = ListNode(cur_val)
            p = p.next

        return dummy.next

    def convertToNumber(self, head):
        p = head
        multi = 1
        res = 0

        while p:
            cur_val = p.val
            res += (cur_val * multi)
            multi *= 10
            p = p.next
        
        return res