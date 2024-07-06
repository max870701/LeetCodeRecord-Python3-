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
    

class Solution1:
    def getFreq(self, s: str) -> List[int]:
        s_freq = [0] * 26
        for char in s:
            pos = ord(char) - ord('a')
            s_freq[pos] += 1
        
        return s_freq

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = len(strs)
        if l == 1:
            return [strs]

        visited_index = set()
        res = []
        for i in range(l):
            if i in visited_index: continue
            tmp = [strs[i]]
            for j in range(i+1, l):
                if j not in visited_index and \
                self.getFreq(strs[i]) == self.getFreq(strs[j]):
                    tmp.append(strs[j])
                    visited_index.add(j)
            
            visited_index.add(i)
            res.append(tmp)

        return res
    

class Solution2:
    def getFreq(self, s: str) -> List[int]:
        s_freq = [0] * 26
        for char in s:
            pos = ord(char) - ord('a')
            s_freq[pos] += 1
        
        return s_freq

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key: freq distribution, Value: list of strings
        d = defaultdict(list)

        for string in strs:
            s_freq = self.getFreq(string)
            d[tuple(s_freq)].append(string)

        return d.values()