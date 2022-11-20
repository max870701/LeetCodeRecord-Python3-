class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        words_reverse = self.reverseWord(s.strip())
        for word in word_reverse.split(" "):
            if word == "": continue
            word_reverse = self.reverseWord(word)
            res += word_reverse + " "
            
        return res.rstrip()
    
    def reverseWord(self, s):
        tmp = ""
        for i in range(len(s) - 1, -1, -1):
            tmp += s[i]
        
        return tmp

    
    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Fastest
        # s.split() to split all string in words (no matter how many space)
        # List slice method. list[start, end, step] (include start, exclude end)
        return " ".join(i for i in s.split()[::-1])