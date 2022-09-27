class Compare(str):
    # > "larger than" comparsion operator
    def __lt__(a, b):
        # Override this operator
        return (a+b) > (b+a)
    
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # map(str, nums) convert to numerical string list
        nums = sorted(map(str, nums), key=Compare)
        
        return str(int("".join(nums))

        
        