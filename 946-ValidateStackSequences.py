class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = []
        p = 0
        
        # When push
        for n in pushed:
            res.append(n)
            # When pop
            while res and p < len(popped) and res[-1] == popped[p]:
                res.pop()
                p += 1
    
        return res == []
    
    
class Solution2:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        for n in pushed:
            pushed[i] = n
            i += 1
            while i > 0 and pushed[i-1] == popped[j]:
                i -= 1
                j += 1
            
        return i == 0