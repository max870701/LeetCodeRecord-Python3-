# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortNumbers(self, _n:int) -> ListNode:
        d = str(_n)
        for i in range(len(d)):
            if i == 0:
                node = ListNode(val=int(d[i]))
            else:
                node = ListNode(val=int(d[i]), next=node)
                
        return node
    
    def reDigital(self, _node:ListNode) -> int:
        temp = 0
        
        for t in range(1, 101):
            if _node == None:return temp
            temp += _node.val * pow(10, t-1)
            _node = _node.next
            
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_1 = self.reDigital(l1)
        number_2 = self.reDigital(l2)
        total = number_1 + number_2
        
        return self.sortNumbers(_n=total)
        
