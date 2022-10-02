# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head): # space complexity O(1)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        current_node = head

        while current_node: # val != None
            # Assign the next node
            next_node = current_node.next
            # The next point to the prev_node
            current_node.next = prev_node
            # Move to next node (right)
            prev_node = current_node
            current_node = next_node

        return prev_node

    def reverseList1(self, head): # fastest, but the space complexity is O(n)
        if head is None: #if input is a empty list
            return head
        if head.next is None: # End condition
            return head # ListNode(val=head.val, next=None)
        
        # Recursively Call reverseList
        # reverse_sub will 
        reverse_sub = self.reverseList1(head=head.next)
        # Assign the next pointer of head.next to head
        head.next.next = head
        # And then assign the next pointer of head to None
        # In order to avoid a cycle
        head.next = None

        # The reverse_sub will refer to
        # the head of the new reverse sub ListNode
        return reverse_sub


    def reverseList2(self, head):
        tmp = None
        while head:
            if tmp:
                tmp = ListNode(val=head.val, next=tmp)
            else:
                tmp = ListNode(val=head.val)
            head = head.next
            
        return tmp

