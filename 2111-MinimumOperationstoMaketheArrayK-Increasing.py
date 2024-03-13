class Solution:
    def __init__(self):
        self.MAXN = 100001
        self.nums = [None] * self.MAXN
        self.ends = [None] * self.MAXN

    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = 0
        for i in range(k):
            size = 0
            # 把每一組數列放入 self.nums
            for j in range(i, n, k):
                self.nums[size] = arr[j]
                size += 1
            # 當前組所需要修改的長度 = 當前組長度 - 當前組最長不下降子序列的長度
            res += size - self.lenOfNoDecreasing(size)

        return res

    def lenOfNoDecreasing(self, size):
        l = 0
        for i in range(size):
            num = self.nums[i]
            find = self.bs(l, num)
            if find == -1:
                self.ends[l] = num
                l += 1
            else:
                self.ends[find] = num
        
        return l

    def bs(self, l, num):
        left = 0
        right = l - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if num < self.ends[mid]:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res