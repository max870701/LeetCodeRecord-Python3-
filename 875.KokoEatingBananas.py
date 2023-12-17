class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles) # 所需檢視的速度範圍
        ans = 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            if self.f(piles, mid) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

    def f(self, piles, speed):
        time = 0
        for pile in piles:
            # 每堆的時間為 pile / speed 向上取整
            time += (pile + speed - 1) // speed
        return time
    