class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time complexity is dominated by the invocation of sort, 
        # which will run in O(nlgn) time for any sensible implementation.
        # Space complexity is O(1)
        if not nums:return 0

        nums.sort()
        longest_streak = 1
        current_streak = 1

        #Trick: use i, i-1 to avoid the out of bound error
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                # Count the streak
                if nums[i] == nums[i-1] + 1:
                    current_streak += 1
                # Record the longest streak and reset current streak
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        
        # If the current_streak is end at the last element in the list
        # We have to return current streak
        return max(longest_streak, current_streak)

    def longestConsecutive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time complexity O(n)
        # Space complexity O(n)
        longest_streak = 0
        num_set = set(nums) # no repeat element

        for num in num_set:
            # Ensure the num is not in any middle of streak
            if num - 1 not in num_set:
                current_streak = 1

                while num + 1 in num_set:
                    current_streak += 1
                    num += 1
                
                longest_streak = max(longest_streak, current_streak)

        return longest_streak