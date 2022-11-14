class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        # Enumerate all indexs
        for i in range(len(s)):
            # s[i] as the center of a palindrome
            s1 = self.palindrome(s, i, i)
            # s[i] and s[i+1] as the center of a palindrome
            s2 = self.palindrome(s, i, i + 1)
            # Update the result
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        
        return res
    
    def palindrome(self, s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l + 1: r]