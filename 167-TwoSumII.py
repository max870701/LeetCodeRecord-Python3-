class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) - 1
        
        while (low < high):
            res = numbers[low] + numbers[high]
            
            if res == target:
                return [low + 1, high + 1]
            elif res < target:
                low += 1
            else:
                high -= 1