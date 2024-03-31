class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = cur_min = cur_max = nums[0]
        for n in nums[1:]:
            tmp = cur_max * n
            cur_max = max(n, cur_max * n, cur_min * n)
            cur_min = min(n, tmp, cur_min * n)

            ans = max(ans, cur_max)
        
        return ans