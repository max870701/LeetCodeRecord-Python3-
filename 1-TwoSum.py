class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """  
        # One-pass Hash Table
        hash_map = {}
        
        for index in range(len(nums)):
            rest = target - nums[index]
            if rest in hash_map:
                return [index, hash_map[rest]]

            hash_map[nums[index]] = index
    
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Two-pass Hash Table
        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = i
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hash_map and hash_map[rest] != i:
                return [i, hash_map[rest]]