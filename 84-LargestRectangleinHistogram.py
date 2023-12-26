class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        n = len(heights)
        r = 0
        ans = 0
        # 遍歷
        for i in range(n):
            # 持續彈出
            while r > 0 and heights[i] <= heights[mono_stack[r-1]]:
                cur = mono_stack.pop()
                r -= 1
                left = -1 if r == 0 else mono_stack[r-1]
                right = i
                ans = max(ans, heights[cur] * (right - left - 1))
            # 壓入
            mono_stack.append(i)
            r += 1
        # 清算
        while r > 0:
            cur = mono_stack.pop()
            r -= 1
            left = -1 if r == 0 else mono_stack[r-1]
            right = n
            ans = max(ans, heights[cur] * (right - left - 1))
        
        return ans