class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        self.row, self.col = len(matrix), len(matrix[0])
        arr = [0] * self.col
        ans = 0
        for row in matrix:
            for j in range(self.col):
                # 數組壓縮，每個 row 當作底計算
                arr[j] = 0 if row[j] == '0' else arr[j] + 1
            # 更新答案
            ans = max(ans, self.largestRectangleArea(arr))
        return ans

    def largestRectangleArea(self, heights):
        # n = self.col
        mono_stack = []
        r = 0
        ans = 0
        # 遍歷
        for i in range(self.col):
            # 持續彈出
            while r > 0 and heights[i] <= heights[mono_stack[r-1]]:
                cur = mono_stack.pop()
                r -= 1
                left = -1 if r == 0 else mono_stack[r-1]
                ans = max(ans, heights[cur] * (i - left - 1))
            # 壓入
            mono_stack.append(i)
            r += 1
        # 清算
        while r > 0:
            cur = mono_stack.pop()
            r -= 1
            left = -1 if r == 0 else mono_stack[r-1]
            ans = max(ans, heights[cur] * (self.col - left - 1))
        
        return ans