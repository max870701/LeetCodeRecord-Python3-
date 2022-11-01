class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_amount = self.removeElement(nums, 0)
        for i in range(zero_amount, len(nums)):
            nums[i] = 0
        return nums
        
        
    def removeElement(self, nums, val):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow