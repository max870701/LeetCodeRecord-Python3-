from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # 大根堆
        heap = []
        nums_sum = 0
        for n in nums:
            heappush(heap, -n)
            nums_sum += n

        # 目標為砍半
        target = nums_sum / 2
        # 操作次數
        op_cnts = 0 
        # 減少量
        minus = 0
        while minus < target:
            cur = heappop(heap) / 2
            heappush(heap, cur)
            minus -= cur
            op_cnts += 1
        
        return op_cnts
    

class Solution2:
    def halveArray(self, nums: List[int]) -> int:
        # 目標
        nums_sum = sum(nums) / 2
        # 大根堆
        heap = [-n for n in nums]
        heapify(heap)
        # 操作次數
        op_cnts = 0
        while nums_sum > 0:
            cur = heappop(heap) / 2
            heappush(heap, cur)
            nums_sum += cur
            op_cnts += 1

        return op_cnts