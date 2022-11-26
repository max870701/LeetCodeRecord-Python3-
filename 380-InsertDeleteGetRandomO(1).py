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

class RandomizedSet1(object):

    def __init__(self):
        self.nums = []
        # Store the index of values in nums List
        self.valToIndex = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # The element already exist
        if val in self.valToIndex:
            return False
        # Not exist
        # Store the index of the nums in valToIndex Hashset
        # And append it into the nunms List
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # val not exist
        if val not in self.valToIndex:
            return False
        # val exist
        # Get the index of the val
        index = self.valToIndex[val]
        self.valToIndex[self.nums[-1]] = index
        # Swap val and the last element in the nums list
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.nums.pop()
        del self.valToIndex[val]
        return True


    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.nums)