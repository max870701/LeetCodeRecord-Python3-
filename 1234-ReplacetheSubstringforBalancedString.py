class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        # 每個字符所需達到的數量 (不多不少)
        balanced_cnt = n / 4
        # 整段自由變
        ans = n
        # 統計詞頻分佈情況 (已知只會有四種:QWER)
        stats = [0] * 4
        self.getStats(s, stats)
        # 統計對應字典
        word_to_num = {'Q': 0, 'W': 1, 'E': 2, 'R': 3}
        #
        r = 0
        for l in range(n):
            # [0, 0) 左閉右開，窗口長度為 0
            # [0, 1) 窗口長度為 1
            # [l, r) => l ... r-1，r為窗口外
            while (r < n) and (not self.isBalanced(r - l, stats, balanced_cnt)):
                # 字符不平衡，滑動右側窗口前，先更新窗口外的詞頻統計
                stats[word_to_num[s[r]]] -= 1
                # 再滑動右側窗口
                r += 1
            # 跳出 while
            # 情況1: r 越界 n 
            # 情況2: 達成平衡
            if self.isBalanced(r - l, stats, balanced_cnt):
                # 更新記錄，最小值
                ans = min(ans, r-l)
            # 滑動左側窗口前先更新窗口外的詞頻統計
            stats[word_to_num[s[l]]] += 1

        return ans 

    # 返回詞頻統計數組
    def getStats(self, string, stats):
        for char in string:
            if char == "Q":
                stats[0] += 1
            elif char == "W":
                stats[1] += 1
            elif char == "E":
                stats[2] += 1
            else:
                stats[3] += 1

    # 給定窗口長度, 窗口外的詞頻統計數組, 每個字符所需數量，返回能否達標
    def isBalanced(self, window, stats, balanced_cnt):
        for i in range(4):
            if stats[i] > balanced_cnt:
                return False
            window -= balanced_cnt - stats[i]
        return window == 0