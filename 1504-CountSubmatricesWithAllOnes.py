from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        self.row, self.col = len(mat), len(mat[0])
        self.heights = [0] * self.col
        ans = 0

        for row in mat:
            for j in range(self.col):
                self.heights[j] = 0 if row[j] == 0 else self.heights[j] + 1
            ans += self.countFromButtom()
        
        return ans
    
    def countFromButtom(self):
        ans = 0
        r = 0
        mono_stack = [] # 棧底小 棧頂大
        # 遍歷
        for i in range(self.col):
            # 彈出結算
            while r > 0 and self.heights[i] <= self.heights[mono_stack[r-1]]:
                cur = mono_stack.pop()
                r -= 1
                if self.heights[i] < self.heights[cur]:
                    left = -1 if r == 0 else mono_stack[r-1]
                    right = i
                    bottom = max(self.heights[i], 0 if left == -1 else self.heights[left])
                    ans += (self.heights[cur] - bottom) * (right - left - 1) * (right - left) // 2
                    
            # 壓棧
            mono_stack.append(i)
            r += 1

        # 清算
        while r > 0:
            cur = mono_stack.pop()
            r -= 1
            left = -1 if r == 0 else mono_stack[r-1]
            right = self.col
            bottom = 0 if left == -1 else self.heights[left]
            ans += (self.heights[cur] - bottom) * (right - left - 1) * (right - left) // 2
        
        return ans