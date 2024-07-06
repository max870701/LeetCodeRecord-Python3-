class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 單調性 -> Binary Search
        # 左閉右閉
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            # 情況 1: 中間值 > 左邊界值 AND 中間值 > 右邊界值 -> 將 m + 1 位置更新為左側搜尋邊界
            if nums[m] > nums[r]:
                l = m + 1
            # 情況 2: 中間值 > 左邊界值 AND 中間值 <= 右邊界值 -> 將 m 位置更新為右側搜尋邊界，因為 m 有可能是最小值
            # 情況 3: 中間值 <= 左邊界值 AND 中間值 <= 右邊界值 -> 將 m 位置更新為右側搜尋邊界，因為 m 有可能是最小值
            else:
                r = m

        # 此時 l == r，為最小值
        return nums[l]