from collections import Counter

class Solution:
    def minIncrementForUnique(self, nums):
        # Time Complexity O(N+M)
        # Space Complexity O(N+M)
        max_val = max(nums)
        count = Counter(nums)
        duplicate = []
        increment = 0

        # why the range is len(nums) + max_val ?
        # If all of elements are the same, such as [1, 5, 5]
        # we have to count (3 + 5) - 1 time
        for n in range(len(nums) + max_val):
            # if a number is duplicate in the nums list
            if count[n] >= 2:
                # if there is a duplicate number
                # N duplicate we store the rest of N-1
                duplicate.extend([n] * (count[n] - 1))
            
            # if the duplicate list is not empty, and 
            # the count[i] position is not taken yet
            elif duplicate and count[n] == 0:
                # Count the difference between number n and the last element in the duplicate list
                # No matter the order the count the difference, the total difference will be the same.
                # e.g. [1, 5, 7, 4, 4, 3, 1]
                # (2 - 4) + (6 - 1) == (6 - 4) + (2 - 1)
                increment += (n - duplicate.pop())
        
        return increment

    def minIncrementForUnique1(self, nums):
        # Time Complexity O(NlogN)
        # Space Complexity O(N)
        nums.sort()
        increment = 0
        for i in range(1, len(nums)):
            pre = nums[i-1]
            cur = nums[i]
            if pre >= cur:
                increment += pre - cur + 1
                nums[i] = pre + 1

        return increment