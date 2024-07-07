# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        1. Find the middle node
        2. Get the next head pointer of the middle node
        3. Reverse the rest of the head in the 2.
        4. Merge two linked lists
        """
        mid_head = self.findMid(head)
        reversed_right_part_list = self.reverseList(mid_head)

        return self.mergeTwoLists(head, reversed_right_part_list)
    
    def mergeTwoLists(self, head1, head2):
        p = dummy = ListNode()
        p1 = head1
        p2 = head2
        count = 0

        while p1 and p2:
            if count % 2 == 0:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
            count += 1
        
        return dummy.next

    def reverseList(self, head):
        if head is None or head.next is None: return head

        reversed_list = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_list

    def findMid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    

class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        1. Find the middle node
        2. Get the next head pointer of the middle node
        3. Reverse the rest of the head in the 2.
        4. Merge two linked lists
        """
        mid_head = self.findMid(head)
        right_part_head = mid_head.next
        mid_head.next = None
        reversed_right_part_list = self.reverseList(right_part_head)

        return self.mergeTwoLists(head, reversed_right_part_list)
    
    def mergeTwoLists(self, head1, head2):
        p = dummy = ListNode()
        p1 = head1
        p2 = head2
        count = 0

        while p1 and p2:
            if count % 2 == 0:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
            count += 1

        if p1 is None:
            p.next = p2
        else:
            p.next = p1
        
        return dummy.next

    def reverseList(self, head):
        if head is None or head.next is None: return head

        reversed_list = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_list

    def findMid(self, head):
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow