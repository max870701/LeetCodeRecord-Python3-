class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        d = Difference(nums=[0 for _ in range(n)]) 
        for booking in bookings:
            d.increment(start=booking[0] - 1,
                        end=booking[1] - 1,
                        val=booking[2])
        return d.result()

class Difference(object):
    def __init__(self, nums):
        self.diff = nums
        # In general situation
        # self.diff = [nums[0]]
        # for i in range(1, len(nums)):
        #     self.diff += [nums[i] - nums[i-1]]
    
    def increment(self, start, end, val):
        self.diff[start] += val
        if end + 1 < len(self.diff):
            self.diff[end + 1] -= val
    
    # Re-construct the number array
    def result(self):
        res = [self.diff[0]]
        for i in range(1, len(self.diff)):
            res += [res[i - 1] + self.diff[i]]
        return res


class Solution2:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        cnt = [0] * (n+2)
        # 構造差分數組
        for book in bookings:
            # [L, R] 範圍上加票
            cnt[book[0]] += book[2]     # L   位置上加票數
            cnt[book[1] + 1] -= book[2] # R+1 位置上減票數
        # 計算前綴和
        for i in range(1, n+1):
            cnt[i] += cnt[i-1]
        
        return cnt[1:n+1]