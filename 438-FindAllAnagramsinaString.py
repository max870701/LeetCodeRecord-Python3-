from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Anagram = Permutation
        need, window = defaultdict(int), defaultdict(int)
        for c in p:
            need[c] += 1

        left = right = 0
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            # Update
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # The condition of shrinking the window
            while (right - left) >= len(p):
                # Determine the current status
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                # Update
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
