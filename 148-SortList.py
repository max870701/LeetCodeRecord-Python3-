'''
Merge Sort Time Complexity O(nlogn)
Divide and Conquer -> Recursion

Skills
1.Using the Fast and Slow pointer approach (876-Middle of the Linked List)
2.Recursively sort each sublist and combine it into a single sorted list (21-Merge Two Sorted Lists)

Step1: Recursion by sortList method itself
    - split to two lists
    - calling sortList for both sides(left side and right side)
    - Set the condition of end
Step2: Split a linked list to two lists 
        by using the fast and slow pointer
Step3: Merge two lists
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return head
        
        list1, list2 = self.getSplit(head=head)
        left = self.sortList(list1)
        right = self.sortList(list2)
        
        return self.merge(l1=left, l2=right)
        
        
    def merge(self, l1, l2):
        tail = head = ListNode()
        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1 is None:
            tail.next = l2
        else:
            tail.next = l1
            
        return head.next
    
    def getSplit(self, head):
        mid = end = head
        t = h = ListNode()
        
        while end and end.next:
            t.next = ListNode(val=mid.val)
            t = t.next
            mid = mid.next
            end = end.next.next
            
        return h.next, mid