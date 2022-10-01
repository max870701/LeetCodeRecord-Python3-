# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Time complexity is O(N)
        # Space complexity is O(N)
        tmp = set()

        while head:
            if head in tmp:break
            tmp.add(head)
            head = head.next
            
        else:
            return False

        return True

    def hasCycle1(self, head):
        # The fast and slow pointer
        # Time complexity is O(n)
        # Space complexity is O(1)
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:return True
        else:
            return False
