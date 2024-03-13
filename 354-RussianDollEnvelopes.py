class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        # 排序策略: 1.寬度由小到大 2.若寬度相同，高度由大到小
        envelopes = sorted(envelopes, key=lambda e: (e[0], -e[1]))
        # 尋找最長嚴格遞增子序列
        ends = [None] * n # 當前所有長度為 i+1 的遞增子序列的最小結尾
        l = 0 # ends 的有效區長度
        for i in range(n):
            num = envelopes[i][1] # 高度
            find = self.binary_search(ends, l, num)
            if find == -1:
                ends[l] = num
                l += 1
            else:
                ends[find] = num
        
        return l
    
    def binary_search(self, ends, l, num):
        left = 0
        right = l - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if ends[mid] >= num:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res