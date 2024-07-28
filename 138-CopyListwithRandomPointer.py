"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return head

        origin_to_new = {None: None}

        p1 = p2 = head

        while p1 is not None:
            origin_to_new[p1] = Node(p1.val)
            p1 = p1.next

        while p2 is not None:
            cur_node = origin_to_new[p2]
            cur_node.next = origin_to_new[p2.next]
            cur_node.random = origin_to_new[p2.random]
            p2 = p2.next

        return origin_to_new[head]