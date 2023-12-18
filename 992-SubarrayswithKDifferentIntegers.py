class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.numsOfMostKinds(nums, k) - self.numsOfMostKinds(nums, k-1)

    # nums list 中有多少種類小於等於k個的子數組
    def numsOfMostKinds(self, nums, k):
        # 題目給的條件是 nums[i] <= nums 的長度
        max_len = 20001
        stats = [0] * max_len
        # 窗口
        l = 0
        kinds = 0
        ans = 0
        for r in range(len(nums)):
            # r剛進，進行統計窗口種類數量
            if stats[nums[r]] == 0:
                kinds += 1
            stats[nums[r]] += 1
            # 當種類超過 k 個，縮減左側窗口
            while kinds > k:
                if stats[nums[l]] == 1:
                    kinds -= 1
                stats[nums[l]] -= 1
                l += 1
            # 達標，更新 ans
            ans +=  r - l + 1
        return ans