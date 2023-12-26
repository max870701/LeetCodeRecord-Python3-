class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        mono_stack = []
        r = 0
        for i in range(n):
            # 彈出條件（與入棧規則有關），結算
            while r > 0 and temperatures[i] > temperatures[mono_stack[r-1]]:
                top = mono_stack.pop()
                r -= 1
                ans[top] = i - top # 天數即是索引差值
            # 壓入
            mono_stack.append(i)
            r += 1
        return ans