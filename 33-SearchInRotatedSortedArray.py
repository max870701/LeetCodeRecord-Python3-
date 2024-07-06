class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 此問題有單調性區間，可以使用二分搜索
        # 確定在索引區間 [l, r] 進行二分搜索
        l = 0
        r = len(nums) - 1

        # 當 l > r 時，搜索結束
        while l <= r:
            # 計算中間點索引
            m = (l + r ) >> 1
            # 若中間點等於目標值，則返回中間點的索引
            if nums[m] == target:
                return m
            # 若 nums[m] < nums[r]，則確定有單調區間 (m, r]，另一個不一定為單調區間為的是 [l, m)
            elif nums[m] < nums[r]:
                # 檢查 target 是否在單調區間 (m, r] 中，若是則更新 l = m + 1，繼續搜索區間 [l, r]
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # 若不在區間 (m, r] 中，即在區間 [l, m) 中，更新 r = m - 1，繼續搜索區間 [l, r]
                else:
                    r = m - 1
            # 若 nums[m] >= nums[r]，則確定有單調區間 [l, m)，另一個不一定為單調區間為的是 (m, r]
            elif nums[m] >= nums[r]:
                # 檢查 target 是否在單調區間 [l, m) 中，若是則更新 r = m - 1，繼續搜索區間 [l, r]
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # 若不在區間 [l, m) 中，即在區間 (m, r] 中，更新 l = m + 1，繼續搜索區間 [l, r]
                else:
                    l = m + 1
        
        return -1