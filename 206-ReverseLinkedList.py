# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        # space complexity O(1)
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

    # 輸入一個節點head，將以head為起點的鏈表反轉，並返回反轉後的頭節點
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if head is None or head.next is None:
            return head
        # 拆解子問題，記錄 head.next 反轉後的頭節點
        reversed_next_head = self.reverseList(head.next)
        # 將當前 reversed_head 鏈表的尾端接回前面鏈表
        head.next.next = head
        # head.next 指向 None
        head.next = None

        return reversed_next_head 

    def reverseList2(self, head):
        tmp = None
        while head:
            if tmp:
                tmp = ListNode(val=head.val, next=tmp)
            else:
                tmp = ListNode(val=head.val)
            head = head.next
            
        return tmp

