# 動態規劃暴力解 O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            ans = max(ans, dp[i])
        
        return ans
    
# 動態規劃 + 二分搜索 O(nlogn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # ends 為 i+1 長度的嚴格遞增子序列結尾
        ends = [None for _ in range(n)]
        # ends有效區長度為 l
        l = 0
        # 遍歷 nums
        for i in range(n):
            find = self.binary_search(ends, l, nums[i])
            # 沒找到，代表要增加 ends 有效區
            if find == -1:
                ends[l] = nums[i]
                l += 1
            # 有找到
            else:
                ends[find] = nums[i]
        
        return l

    # 給定 ends，找出大於等於 num 的最左位置
    def binary_search(self, ends, l, num):
        # 返回值 ans，若沒找到則返回 -1
        ans = -1
        # 左閉右閉
        left, right = 0, l - 1
        while left <= right:
            mid = left + (right - left) // 2
            if ends[mid] >= num:
                ans = mid
                right = mid - 1
            else: # ends[mid] <= num
                left = mid + 1

        return ans