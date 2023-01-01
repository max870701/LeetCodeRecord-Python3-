class Solution(object):
    def NSum(self, n, nums, start, target):
        size = len(nums)
        res = []
        if (n < 2) or (size < n): return res
        
        nums.sort()
        if n == 2:
            lo, hi = start, size - 1
            while lo < hi:
                s = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if s < target:
                    while (lo < hi) and (nums[lo] == left):
                        lo += 1
                elif s > target:
                    while (lo < hi) and (nums[hi] == right):
                        hi -= 1
                else: # s == target
                    res.append([left, right])
                    while (lo < hi) and (nums[lo] == left):
                        lo += 1
                    while (lo < hi) and (nums[hi] == right):
                        hi -= 1
        else: # If n > 2, do recursion
            i = 0
            while i < size: 
                sub = self.NSum(nums, n-1, i+1, target - nums[i])
                for arr in sub:
                    res.append([nums[i]] + arr)
                while i < size - 1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1

        return res
