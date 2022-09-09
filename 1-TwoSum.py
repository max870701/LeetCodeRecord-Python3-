class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        mapping = {}
        
        for index in range(len(nums)):
            rest = target - nums[index]
            if rest in mapping:
                return [index, mapping[rest]]
            mapping[nums[index]] = index
