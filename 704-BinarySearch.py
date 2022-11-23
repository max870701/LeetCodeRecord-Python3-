class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        # Terminate condition is left = right + 1
        while left <= right:
            # Avoid the overflow
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # The rest part is [mid+1, right], due to [mid] has been searched
                left = mid + 1
            elif nums[mid] > target:
                # The rest part is [left, mid-1], due to [mid] has been searched
                right = mid - 1

        return -1