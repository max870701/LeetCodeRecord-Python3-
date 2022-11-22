from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str The target of permutations
        :type s2: str The whole string
        :rtype: bool
        """
        need, window = defaultdict(int), defaultdict(int)
        for c in s1:
            need[c] += 1

        left = right = 0
        valid = 0
        
        while right < len(s2):
            # char c is the character moved into the window
            c = s2[right]
            # increase the window
            right += 1
            # Update your data below
            if c in need:
                window[c] += 1
                if window[c] == need[c]: # with the same amount
                    valid += 1

            # Debugging output
            # print("Window: [{}, {})\n".format(left, right))

            # Determine if the left side of window need be shrinked
            while (right - left) >= len(s1):
                if valid == len(need):
                    return True
                # char d will be removed from the window
                d = s2[left]
                # Shrink the window
                left += 1
                # Update the data in the window
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
