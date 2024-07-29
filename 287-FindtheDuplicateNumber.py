class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Medium: https://pse.is/69srfy
        # Time: O(n)
        # Space: O(1)

        # Step 1: Find the intersection of two pointers
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Step 2: Find the entrance of the cycle
        # 將 fast 指針放回初始位置，並開始一次走一步
        fast = 0
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow