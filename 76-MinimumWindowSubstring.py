from collections import defaultdict
import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, window = defaultdict(int), defaultdict(int)
        # Can also use collections.Counter(t), but slower
        for c in t:
            need[c] += 1
            
        left = right = 0
        valid = 0
        start = 0
        length = sys.maxint
        
        while right < len(s):
            c = s[right]
            right += 1
            
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if (length == sys.maxint) else s[start:start+length]

class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or len(t) == 0:
            return ""
        s_ascii = [ord(c) for c in s]
        cnt = [0] * 128
        for c in t:
            cnt[ord(c)] -= 1
        # min_len 用於記錄最小覆蓋子串的長度
        min_len = float('inf')
        # start 用於記錄最小覆蓋子串的起始位置
        start = 0
        # 總共欠的字串數量
        debt = len(t)
        # 左邊界
        l = 0
        for r in range(len(s_ascii)):
            # 若此char在cnt中為所欠缺的char，則消去 debt -= 1
            if cnt[s_ascii[r]] < 0:
                debt -= 1
            # cnt 中加上該 char
            cnt[s_ascii[r]] += 1
            # 當 debt 來到 0，開始縮小左邊界，並更新 min_len 和 start 的值
            if debt == 0:
                while cnt[s_ascii[l]] > 0:
                    cnt[s_ascii[l]] -= 1
                    l += 1
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start = l

        return "" if min_len == float('inf') else s[start:start+min_len]