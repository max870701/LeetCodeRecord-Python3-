class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        p1, p2 = 0, 0
        while p1 < len(houses):
            while not self.best(houses, heaters, p1, p2):
                p2 += 1
            ans = max(ans, abs(houses[p1] - heaters[p2]))
            p1 += 1
        return ans

    # 判斷 i 位置的 house 和 j 位置的 heaters 是否為最優距離
    def best(self, houses, heaters, i, j):
        # 情況1: j 位置已經是最後面的位置了
        # 情況2: 下一個 heaters (j+1)與 houses i 的距離大於當前位置 j 的
        return (j == len(heaters) - 1) or (abs(houses[i] - heaters[j+1]) > abs(houses[i] - heaters[j]))