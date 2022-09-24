'''
Linked List
Observe the linked list [1, 3, 5, 6, 7]
The fast and slow pointer: iterating by different steps
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        end = head
        
        while (end is not None) and end.next: # 3 4 1 5 6 8
            middle = middle.next
            end = end.next.next
            
        return middle