# 較慢
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = ListNode(0)
        cur = root
        q = PriorityQueue()
        
        for i, node in enumerate(lists):
            if node:
                q.put((node.val, i, node))
        
        while q.qsize():
            _, i, cur.next = q.get()
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, i, cur.next))
        
        return root.next

# 較快
from heapq import *
class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        if not heap:
            return None

        _, i, head_node = heappop(heap)
        pointer = head_node
        if pointer.next:
            heappush(heap, (pointer.next.val, i, pointer.next))

        while heap:
            _, i, cur_node = heappop(heap)
            pointer.next = cur_node
            pointer = cur_node
            if cur_node.next:
                heappush(heap, (cur_node.next.val, i, cur_node.next))

        return head_node
    
class Solution3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        dummy = ListNode(-1)
        pointer = dummy

        while heap:
            _, i, cur_node = heappop(heap)
            pointer.next = cur_node
            pointer = cur_node
            if cur_node.next:
                heappush(heap, (cur_node.next.val, i, cur_node.next))

        return dummy.next