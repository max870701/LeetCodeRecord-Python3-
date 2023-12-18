class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(list, i, j):
            list[i], list[j] = list[j], list[i]
        # l 左側皆為符合 i index上存在 i+1 的數值
        l = 0
        # r 開始向右為垃圾區
        # 假設當前能將 1~r 完整收集 
        r = len(nums)
        while l < r:
            if nums[l] == l+1:
                l += 1
            # 換到垃圾區
            # 情況1: nums[l] <= l，由初始定義 l 左側皆符合 i index 上存在 i+1 的數值，即 l 已經存在或是為非正整數
            # 情況2: nums[l] > r，超出目標收集範圍 1~r
            # 情況3: nums[nums[l] - 1] == nums[l]，存在重複值，需下修目標範圍
            elif (nums[l] <= l) or (nums[l] > r) or (nums[nums[l] - 1] == nums[l]):
                r -= 1
                swap(nums, l, r)
            # 非垃圾區情況，交換至應該放置的index上
            else:
                swap(nums, l, nums[l] - 1)

        return l + 1