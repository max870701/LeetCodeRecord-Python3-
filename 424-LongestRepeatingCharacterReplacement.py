class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency of the char in the sliding window
        char_freq = {}
        # Result of max length of the replaced substring
        res = 0

        l = 0
        for r in range(len(s)):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1
            # The condition of shrinking the window
            while (r - l + 1) - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res