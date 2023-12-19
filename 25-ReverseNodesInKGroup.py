# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 返回從 head 開始的 k-Group 反轉鏈表
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None
        a = b = head
        for _ in range(k):
            # Base Case: 當 head 鏈表長度不足 k，則不需要反轉
            if b is None:
                return head
            # 移動
            b = b.next
        # 記錄反轉後的K-group
        new_group_head = self.reverse(a, b)
        # 接起來
        a.next = self.reverseKGroup(b, k)

        return new_group_head

    
    # 反轉 [a, b) 間的鏈表，並返回鏈表頭節點
    def reverse(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = a
        next_node = None

        while cur_node != b:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        
        return prev_node