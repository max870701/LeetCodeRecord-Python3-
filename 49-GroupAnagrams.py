from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time O(N * K logK)
        # Space O(N * K)
        res = defaultdict(list)
        
        for string in strs:
            res[tuple(sorted(string))].append(string)

        return res.values()

    def groupAnagrams1(self, strs):
        # Time O(N * K)
        # Space O(N * K)

        # create a default dictionary to avoid key error
        res = defaultdict(list)

        for string in strs:
            # correspond to 26 alphabet (A-Z)
            count = [0] * 26
            
            for char in string:
                # use ord() to get the unicode of a char
                # ord('a') is 97, ord('z') is 122
                count[ord(char) - ord('a')] += 1
            
            res[tuple(count)].append(string)
        
        return res.values()
