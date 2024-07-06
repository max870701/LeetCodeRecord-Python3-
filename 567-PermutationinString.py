class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[r]) - ord('a')
            s2_freq[index] += 1

            if s2_freq[index] == s1_freq[index]:
                matches += 1
            elif s2_freq[index] - 1 == s1_freq[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2_freq[index] -= 1

            if s2_freq[index] == s1_freq[index]:
                matches += 1
            elif s2_freq[index] + 1 == s1_freq[index]:
                matches -= 1

            l += 1
        
        return matches == 26


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