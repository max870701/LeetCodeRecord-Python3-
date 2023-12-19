# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # ln1, ln2
        head1, head2 = ListNode(-1), ListNode(-1)
        ln1, ln2 = head1, head2

        while head:
            if head.val < x:
                ln1.next = ListNode(head.val)
                ln1 = ln1.next
            else:
                ln2.next = ListNode(head.val)
                ln2 = ln2.next
            head = head.next
        
        ln1.next = head2.next

        return head1.next