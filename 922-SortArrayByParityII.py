class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        def swap(list, i, j):
            list[i], list[j] = list[j], list[i]
        even, odd = 0, 1
        n = len(nums)
        while even < n and odd < n:
            if (nums[n-1] & 1) == 1:
                swap(nums, odd, n-1)
                odd += 2
            else:
                swap(nums, even, n-1)
                even += 2
        return nums