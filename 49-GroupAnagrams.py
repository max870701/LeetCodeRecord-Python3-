class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time O(N * K logK)
        # Space O(N * K)
        res = collections.defaultdict(list)
        
        for string in strs:
            res[tuple(sorted(string))].append(string)

        return res.values()

    def groupAnagrams1(self, strs):
        # Time O(N * K)
        # Space O(N * K)
        pass
