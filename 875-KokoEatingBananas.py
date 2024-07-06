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


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # F(k) -> hours
        def eatingHours(piles, e_speed):
            hours = 0
            for b_amount in piles:
                hours += (b_amount // e_speed)
                if b_amount % e_speed != 0:
                    hours += 1
            
            return hours

        # Ensure the range of k
        k_left = 1
        k_right = max(piles)

        # Binary Search
        while k_left <= k_right:
            k_mid = k_left + (k_right - k_left) // 2
            total_time = eatingHours(piles, k_mid)
            
            if total_time <= h:
                k_right = k_mid - 1

            elif total_time > h:
                k_left = k_mid + 1

        return k_left