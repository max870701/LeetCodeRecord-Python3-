class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Key: 出現頻率（最長不超過 nums 長度）, Value: 對應的數字列表
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] += 1
        
        for n, t in count.items():
            freq[t].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res