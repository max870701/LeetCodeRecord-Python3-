class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        s_ascii = [ord(c) for c in s]
        ans = 0
        # 有 require 種字符達到 k 次重複，遍歷所有 require種 的可能性
        for require in range(1, 27):
            # 統計詞頻
            stats = [0] * 128
            # 當前蒐集到的字符種類
            collect = 0
            # 達到 k 次的字符種類
            satisfy = 0
            l = 0
            for r in range(n):
                # r 進入
                stats[s_ascii[r]] += 1
                # 判斷 collect 和 satisfy
                if stats[s_ascii[r]] == 1:
                    collect += 1
                if stats[s_ascii[r]] == k:
                    satisfy += 1
                # 若 collect 的種類超過 require 種，則不斷縮減左側窗口
                while collect > require:
                    # 若移出後 stats[s_ascii[l]] 為 0，則減少 collect -= 1
                    if stats[s_ascii[l]] == 1:
                        collect -= 1
                    # 若移出後 stats[s_ascii[l]] 少於 k 次門檻，則減少 satisfy -= 1
                    if stats[s_ascii[l]] == k:
                        satisfy -= 1
                    stats[s_ascii[l]] -= 1
                    # 移動窗口
                    l += 1
                # 符合 require 種，l..r，子串以r結尾且最長的子串
                if satisfy == require:
                    ans = max(ans, r - l + 1)
        
        return ans