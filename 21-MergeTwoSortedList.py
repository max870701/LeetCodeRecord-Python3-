# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Solution1: Recursion
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:return list2
        if list2 is None:return list1
        
        if list1.val <= list2.val:
            new_list = list1
            list1 = list1.next
        else:
            new_list = list2
            list2 = list2.next
            
        new_list.next = self.mergeTwoLists(list1=list1, list2=list2)
        
        return new_list
    
    # Solution2: Iterative
    def mergeTwoLists_2(self, list1, list2):
        tail = head = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1 is None:
            tail.next = list2
        else:
            tail.next = list1
        
        return head.next