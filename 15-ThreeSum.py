class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        # nums = [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            # nums[i] 數字大於0，跳出for loop
            # 因為三數之和要為0，第一個數字必須小於等於0
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum2(nums, i, res)

        return res

    
    def twoSum1(self, nums, i, res):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            sumThree = nums[i] + nums[lo] + nums[hi]
            if sumThree < 0:
                lo += 1
            elif sumThree > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi+1]:
                    hi -= 1

    def twoSum2(self, nums, i, res):
        hashset = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in hashset:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            hashset.add(nums[j])
            j += 1

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, dups = set(), set()
        seen = {}
        for i, val in enumerate(nums):
            if val not in dups:
                dups.add(val)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val, val2, complement))))
                    seen[val2] = i
        return res

    def threeSum3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        i = 0
        res = []
        while i < n:
            tuples = self.twoSum(nums, i+1, 0 - nums[i])
            for t in tuples:
                res.append([nums[i]] + t)
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res


    def twoSum3(self, nums, start,  target):
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
    
# nSum 遞歸寫法
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.n = len(nums)
        return self.nSum(nums, 3, 0, 0)
    
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