from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = defaultdict(int)

        left = right = 0
        res = 0

        while right < len(s):
            c = s[right]
            right += 1
            # Update window
            window[c] += 1
            # The condition of shrinking the window
            # If the character is repeated
            while (window[c] > 1):
                d = s[left]
                left += 1
                # Update
                window[d] -= 1
            res = max(res, right - left)

        return res

    
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_ascii = [ord(c) for c in s]
        s_last = [-1] * 128
        ans = 0
        l = 0
        for r in range(len(s)):
            l = max(l, s_last[s_ascii[r]] + 1)
            ans = max(ans, r - l + 1)
            s_last[s_ascii[r]] = r
        return ans
    
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_ascii = [ord(c) for c in s]
        s_last = [-1] * 128
        ans = 0
        l = 0
        for r, c in enumerate(s_ascii):
            l = max(l, s_last[c] + 1)
            ans = max(ans, r - l + 1)
            s_last[c] = r

        return ans