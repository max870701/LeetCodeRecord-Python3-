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
            