# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.successor = None

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Base Case
        if left == 1:
            return self.reverseN(head, right)
        # 區間距離恆為 right - left + 1
        # 區間往前移動，退階為base case
        head.next = self.reverseBetween(head.next, left-1, right-1)
        
        return head
        

    # 給定頭節點 head，返回反轉前 n 個節點的鏈表頭節點
    def reverseN(self, head, n):
        # 類似反轉整個單鏈表
        # Base case
        if n == 1:
            self.successor = head.next
            return head
        # 記錄反轉後的鏈表頭節點
        reversed_head = self.reverseN(head.next, n-1)
        # 重置當前 head 指向
        head.next.next = head
        head.next = self.successor
        
        return reversed_head

class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        dummy = head
        
        while dummy:
            arr.append(dummy)
            dummy = dummy.next
        
        while left < right:
            lnode, rnode = arr[left-1], arr[right-1]
            lnode.val, rnode.val = rnode.val, lnode.val
            left += 1
            right -= 1
        
        return head