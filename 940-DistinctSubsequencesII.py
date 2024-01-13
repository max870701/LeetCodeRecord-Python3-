class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 1000000007
        cnt = [0] * 26
        all = 1
        for c in s:
            index = ord(c) - ord('a')
            newAdd = (all - cnt[index] + mod) % mod
            cnt[index] = (cnt[index] + newAdd) % mod
            all = (all + newAdd) % mod
        
        return (all - 1 + mod) % mod