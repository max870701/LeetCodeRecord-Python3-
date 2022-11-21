# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.left = head
        return self.traverse(head)
    
    
    def traverse(self, right):
        if right is None:
            return True
        # Recursion
        global res
        res = self.traverse(right.next)
        # From the end
        # boolean operation
        res = (res) and (right.val == self.left.val)
        self.left = self.left.next
        return res


    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Use fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Contain odd elements in the ListNode
        if fast:
            slow = slow.next
        
        left = head
        # The reverse of the ListNode which starts at slow pointer
        # Should be the same as the first half of the input ListNode
        right = self.reverse(slow)
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        
        return True
        
    
    def reverse1(self, head):
        pre, cur = None, head
        while cur:
            # Modify the pointer first, and then the previous value and current value
            tmp_next = cur.next
            cur.next = pre
            pre = cur
            cur = tmp_next
        
        return pre