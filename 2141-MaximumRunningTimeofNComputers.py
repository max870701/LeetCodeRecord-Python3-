class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # 能撐的分鐘範圍
        left, right = 0, sum(batteries)
        ans = 0
        while left <= right:
            mid = left + ((right - left) >> 1)
            if self.f1(batteries, n, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    # 是否能讓 n 台電腦維持 time 分鐘
    def f1(self, batteries, n, time):
        sum_cap = 0
        for battery in batteries:
            if battery > time:
                n -= 1
            else:
                sum_cap += battery
            if sum_cap >= n * time:
                return True
        return False

class Solution2:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # 能撐的分鐘範圍
        max_battery = max(batteries)
        sum_cap = sum(batteries)
        if sum_cap > max_battery * n:
            # 若 sum_cap > max_battery * n
            # 代表能撐的分鐘數一定大於 max_battery 的分鐘數，那麼所有電池的電量皆可視為碎片電池(皆可拼接)
            # 用 sum_cap / n 得出 n 台電腦的最長的同時運行時間
            return sum_cap // n
        ans = 0
        # 能撐的分鐘範圍，右邊範圍縮減至 max_battery
        left, right = 0, max_battery
        while left <= right:
            mid = left + ((right - left) >> 1)
            if self.f1(batteries, n, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    # 是否能讓 n 台電腦維持 time 分鐘
    def f1(self, batteries, n, time):
        sum_cap = 0
        for battery in batteries:
            if battery > time:
                n -= 1
            else:
                sum_cap += battery
            if sum_cap >= n * time:
                return True
        return False