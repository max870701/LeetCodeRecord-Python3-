class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if nums is None and len(nums) < 2: return -1
        # 轉換為找入環節點
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 將 fast 指針放回初始位置，並開始一次走一步
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow