class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        i = 0
        self.size = len(nums)
        while i < self.size:
            triples = self.threeSum(nums, i+1, target - nums[i])
            for t in triples:
                res.append([nums[i]] + t)
            while (i < self.size - 1) and (nums[i] == nums[i+1]):
                i += 1
            i += 1
        return res          

    def threeSum(self, nums, start, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = start
        while i < self.size:
            tuples = self.twoSum(nums, i+1, target - nums[i])
            for t in tuples:
                res.append([nums[i]] + t)
            while i < self.size-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res


    def twoSum(self, nums, start,  target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        left, right = start, len(nums) - 1
        
        while left < right:
            sum_num = nums[left] + nums[right]
            left_num, right_num = nums[left], nums[right]
            if sum_num < target:
                while (left < right) and (nums[left] == left_num):
                    left += 1
            elif sum_num > target:
                while (left < right) and (nums[right] == right_num):
                    right -= 1
            else: # sum_num == target
                res.append([left_num, right_num])
                while (left < right) and (nums[left] == left_num):
                    left += 1
                while (left < right) and (nums[right] == right_num):
                    right -= 1
        return res
    
# 遞歸解決 nSum 問題
class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.n = len(nums)
        return self.nSum(nums, 4, 0, target)
    
    # 給定 nums, n , start, target，返回 k 個數字的總和為 target 的所有 List[List[int]]
    def nSum(self, nums, k, start, target):
        res = []
        if k < 2 or self.n < k:
            return res
        
        # Base case 為 twoSum
        if k == 2:
            left, right = start, self.n - 1
            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        else:
            # k > 2, 遞歸調用 (n-1)Sum
            for i in range(start, self.n):
                if i == start or (i > start and nums[i] != nums[i - 1]):
                    sub = self.nSum(nums, k - 1, i + 1, target - nums[i])
                    for arr in sub:
                        res.append([nums[i]] + arr)

        return res