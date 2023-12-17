class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.searchLeftBound(nums, target), self.searchRightBound(nums, target)]
        
    
    def searchLeftBound(self, nums, target):
        # 左閉右開 [left, right)
        left = 0
        right = len(nums)
        # Stop at left == right
        while left < right:
            # Avoid the overflow
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                right = mid
        # if left == right, but not found the target
        if left == len(nums): return -1
        # if left == 0 but nums[left] != target
        return left if nums[left] == target else -1

    def searchRightBound(self, nums, target):
        # 左閉右開 [left, right)
        left = 0
        right = len(nums)
        # Stop at left == right
        while left < right:
            # Avoid the overflow
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid + 1
                # mid - 1 = left
            elif nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                left = mid + 1
        if (left - 1) < 0: return -1
        return (left - 1) if (nums[left-1] == target) else -1
    

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchLeftBound(nums, target), self.searchRightBound(nums, target)]

    def searchLeftBound(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return ans

    def searchRightBound(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return ans