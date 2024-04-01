# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        node = head.next
        
        while node:
            next_node = node.next

            if node.val >= 0:
                prev = prev.next
            else: # node.val < 0
                node.next = head
                head = node
                prev.next = next_node

            node = next_node
    
        return head