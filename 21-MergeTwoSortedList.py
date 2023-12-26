# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 遞迴寫法
class Solution:
    # 給定 list1, list2 返回 merge 後的 list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if list1 is None: return list2
        if list2 is None: return list1
        
        # 遞迴
        if list1.val <= list2.val:
            ans = list1
            list1 = list1.next
        else:
            ans = list2
            list2 = list2.next

        ans.next = self.mergeTwoLists(list1, list2)
        return ans

# 迭代寫法
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: return list2
        if list2 is None: return list1

        dummy = ListNode(-1)
        # 新鏈表的指針
        p = dummy
        # list1 的指針
        p1 = list1
        # list2 的指針
        p2 = list2

        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1 is None:
            p.next = p2
        if p2 is None:
            p.next = p1
        
        return dummy.next