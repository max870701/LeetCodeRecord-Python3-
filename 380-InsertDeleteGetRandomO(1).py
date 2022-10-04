from random import choice

class RandomizedSet(object):

    def __init__(self):
        self.set = set()
        # self.dict = {}
        # self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

        # if val in self.dict:
        #    return False
        # self.dict[val] = len(self.list)
        # self.list.append(val)
        # return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False
        
        # if val in self.dict:
        #     last, i = self.list[-1], self.dict[val]
        #     self.list[i] = last
        #     self.dict[last] = i
        #     self.list.pop()
        #     del self.dict[val]
        #     return True
        # return False

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(tuple(self.set))
        
        # return choice(self.list)


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()