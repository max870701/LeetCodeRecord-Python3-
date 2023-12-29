class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 單調棧: 棧底大-棧頂小
        mono_stack = []
        r = 0
        ans = [-1] * n
        # 遍歷兩遍環形數組
        for i in range(2*n):
            # 彈出條件
            while r > 0 and nums[mono_stack[r-1]] < nums[i%n]: # 取模
                cur = mono_stack.pop()
                r -= 1
                ans[cur] = nums[i%n]
            # 壓入條件
            mono_stack.append(i%n)
            r += 1
        
        return ans