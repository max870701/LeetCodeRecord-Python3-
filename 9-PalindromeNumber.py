class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        # x :     12321
        # offset: 10000
        offset = 1
        while x // offset >= 10:
            offset *= 10
        # Count
        while x != 0:
            if (x // offset) != (x % 10): return False
            x = (x % offset) // 10
            offset /= 100

        return True

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]