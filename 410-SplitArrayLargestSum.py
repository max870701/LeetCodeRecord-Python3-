class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = 0, sum(nums)
        ans = 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            if self.f(nums, mid) <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
    def f(self, nums, limit):
        parts = 1
        tmp_sum = 0
        for num in nums:
            if num > limit:
                return float('inf')
            if (tmp_sum + num > limit):
                parts += 1
                tmp_sum = num
            else:
                tmp_sum += num
        return parts
    
    
class Solution2(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.shipWithinDays(nums,k)
    
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # 左閉右開
        # 取 list 中最大，分 len(weights) 天運完
        left = max(weights)
        # right 一天運完（全包）
        right = sum(weights) + 1

        while left < right:
            mid = (right + left) / 2
            if (self.f(weights, mid) <= days):
                right = mid
            else:
                left = mid + 1

        return left


    def f(self, weights, x):
        '''
        定義：運載能力為 x 時，需要 f(x) 天運完
        f(x) 隨 x 的增加單調遞減
        '''
        days = 0
        i = 0
        l = len(weights)
        while i < l:
            cap = x
            while i < l:
                if cap < weights[i]:
                    break
                else:
                    cap -= weights[i]
                i += 1
            days += 1
        return days