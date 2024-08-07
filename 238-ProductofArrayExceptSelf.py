class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        for i in range(1, l):
            # Update Prefix
            res[i] = res[i-1] * nums[i-1]

        suffix = 1
        for j in range(l-2, -1, -1):
            # Update Suffix
            suffix *= nums[j+1]
            # Update the result
            res[j] *= suffix

        return res