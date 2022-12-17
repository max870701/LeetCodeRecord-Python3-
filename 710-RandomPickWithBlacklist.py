from random import randrange
class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.mapping = {}
        self.sz = n - len(blacklist)
        for b in blacklist:
            self.mapping[b] = 777
        
        last = n - 1
        for b in blacklist:
            if b >= self.sz: continue
            while last in self.mapping:
                last -= 1
            self.mapping[b] = last
            last -= 1

    def pick(self):
        """
        :rtype: int
        """
        index = randrange(self.sz)
        if index in self.mapping:
            return self.mapping[index]
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()