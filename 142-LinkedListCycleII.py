# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from numpy import intersect1d


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = set()
        while head:
            if head in tmp:
                return head
            tmp.add(head)
            head = head.next
        else:
            return None

    def detectCycle1(self, head):
        """
        Floyd's Tortoise and Hare
        <Phase 1>
        Hare :fast pointer
        Tortoise :slow pointer
        Assume the length of the cycle is C, we have the nodes 0 to C-1
        The noncyclic nodes have been labelled from -F to -1 (index),
        where F is the number of nodes outside of the cycle.

        Tortois -> the node 0 (it moves F steps)
        Hare -> the node h (it moves 2F steps),
        After meet the 0 node, it moves F steps and eventually get to the h node
        So F = h + nC, we have F - h = nC
        
        After (C-h) more iterations,
        Tortois -> from node 0 to (C - h)
        Hare -> from node h to (C - h), because the start postition h plus the steps 2(C - h),
        it will be h + 2C - 2h = 2C - h = C - h

        Hence, Torotis and Hare will eventually meet at the same node (C - h)
        The intersection is (C - H)
        
        <Phase 2>
        Given that phase 1 finds an intersection, phase 2 proceeds to find the node that is the entrance to the cycle

        By initializing two more pointers
        ptr1, -F node, which points to the head of the list
        ptr2, (C - h) node, which points to the intersection

        Then move each of them by 1 step
        When ptr1 moves F steps from -F to the 0 node
        ptr2 also moves F steps from (C - h), so it will be F + (C - h)
        Due to we already know F - h = nC, we have (n+1)C, which is the 0 node
        """
        if head is None:return None
        if self.getIntersect(head=head) is None:return None

        ptr1 = head
        ptr2 = intersect1d

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
    
    def getIntersect(self, head):
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        else:
            return None