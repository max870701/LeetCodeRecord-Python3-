from sys import last_value


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for n in nums:
            if nums[i] == val:
                nums.pop(i)
                nums.append(-1)
            else:
                i += 1
        return i

    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        writer = 0
        reader = 0
        while reader < len(nums):

            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1

            reader += 1

        return writer

    def removeElement3(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        writer = 0
        reader = 0
        while reader < len(nums):

            if nums[reader] == val:
                reader += 1
                continue
            else:
                nums[writer] = nums[reader]
                writer += 1

            reader += 1

        return writer

    def removeElement4(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0 # The first pointer starts at 0 position
        l = len(nums) # The second pointer starts at the last position
        while i < l:
            if nums[i] == val:
                nums[i] = nums[l - 1] # swap
                l -= 1
            else:
                i += 1
        return l

    def removeElement5(self, nums, val):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow