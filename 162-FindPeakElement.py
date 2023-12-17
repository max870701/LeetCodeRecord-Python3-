class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        # If index 0 is a peak
        if nums[0] > nums[1]:
            return 0
        # If index n-1 is a peak
        if nums[n-1] > nums[n-2]:
            return n-1
        # If both index 0, n-1 are not peak
        left, right = 1, n-2
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid-1]:
                right = mid - 1
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                ans = mid
                break
        return ans