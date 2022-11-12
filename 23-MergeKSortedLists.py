from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = ListNode(0)
        cur = root
        q = PriorityQueue()
        
        for node in lists:
            if node:
                q.put((node.val,id(node), node))
        
        while q.qsize()>0:
            cur.next = q.get()[2]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, id(cur.next), cur.next))
        
        return root.next