class Solution:
    # 指定 k 的數字的和要等於 n ，返回所有可能的組合
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.track = []
        self.target = n
        self.trackSum = 0
        self.cnt = k
        nums = [ i for i in range(1, 10)] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.backtrack(nums, 0)
        return self.ans

    def backtrack(self, nums, start):
        if self.cnt == 0:
            if self.trackSum == self.target:
                self.ans.append(self.track[:])
            return

        for i in range(start, 9):
            self.track.append(nums[i])
            self.trackSum += nums[i]
            self.cnt -= 1
            self.backtrack(nums, i+1)
            self.track.pop()
            self.trackSum -= nums[i]
            self.cnt += 1