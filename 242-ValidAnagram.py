# Time Complexity: O(S + T)
# Space Complexity: O(1)
class Solution:
    def getFreq(self, s: str) -> List[int]:
        s_freq = [0] * 26
        for char in s:
            pos = ord(char) - ord('a')
            s_freq[pos] += 1
        
        return s_freq

    def isAnagram(self, s: str, t: str) -> bool:
        return self.getFreq(s) == self.getFreq(t)
    
# Space Complexity: O(1)
