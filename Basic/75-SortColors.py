class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Using three pointers
        # p0 is the right boundry of 0 list (sorted)
        # p2 is the left boundry of 2 list (sorted)
        current = 0
        p0 = 0
        p2 = len(nums) - 1
        
        while current <= p2:
            if nums[current] == 0:
                nums[current], nums[p0] = nums[p0], nums[current]
                p0 += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[p2] = nums[p2], nums[current]
                p2 -= 1
            else: # nums[current] == 1
                current += 1
            
        return nums
                