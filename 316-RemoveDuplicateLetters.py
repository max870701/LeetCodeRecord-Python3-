class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        MAXN = 26
        cnts = [0] * MAXN         # 字符計數器
        mono_stack = [''] * MAXN  # 單調棧
        enter = [False] * MAXN    # 記錄字母是否在棧中
        r = 0                     # 單調棧大小
        # 詞頻統計
        for char in s:
            cnts[ord(char)-ord('a')] += 1
        # 遍歷
        for cur in s:
            # 每個字符只能出現一次
            if not enter[ord(cur) - ord('a')]:
                # 彈出條件
                while (r > 0) and (ord(mono_stack[r-1]) > ord(cur)) and (cnts[ord(mono_stack[r-1]) - ord('a')] > 0):
                    enter[ord(mono_stack[r-1]) - ord('a')] = False
                    r -= 1
                # 沒有進入過 mono_stack 才能壓棧
                mono_stack[r] = cur
                r += 1
                enter[ord(cur) - ord('a')] = True
            # 減少字符計數
            cnts[ord(cur) - ord('a')] -= 1
        
        return ''.join(mono_stack[:r])