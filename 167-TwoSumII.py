class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers 為升序列表
        # 左右指針
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []