class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = 1000000000 + 1

        while left < right:
            mid = (left + right) / 2
            print(self.f(piles, mid))
            if (self.f(piles, mid) == h):
                right = mid
            elif (self.f(piles, mid) < h):
                # let f(x) bigger, it means let x smaller
                right = mid
            elif (self.f(piles, mid) > h):
                # let f(x) smaller, it means let x bigger
                left = mid + 1
        return left

    def f(self, piles, x):
        hours = 0
        for i in range(len(piles)):
            hours += piles[i] / x
            if piles[i] % x > 0:
                hours += 1
        return hours

    