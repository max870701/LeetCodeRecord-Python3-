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