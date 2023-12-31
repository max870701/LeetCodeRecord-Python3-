from queue import Queue
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # 鄰接表建圖，以字母搜尋
        graph = [[] for _ in range(26)]
        for sticker in stickers:
            sticker = self.sortString(sticker)
            for i in range(len(sticker)):
                if i == 0 or sticker[i] != sticker[i-1]:
                    char = sticker[i]
                    graph[ord(char) -  ord('a')].append(sticker)
        # 記錄訪問過的 target
        visited = set()
        # 排序 target
        target = self.sortString(target)
        # 層序遍歷
        level = 1
        q = Queue()
        q.put(target)
        while not q.empty():
            size = q.qsize()
            for _ in range(size):
                cur_target = q.get()
                for sticker in graph[ord(cur_target[0]) - ord('a')]:
                    res = self.tailor(cur_target, sticker)
                    if not res:
                        return level
                    elif res not in visited:
                        visited.add(res)
                        q.put(res)
            level += 1
        return -1

    def tailor(self, target, sticker):
        # 雙指針處理 target 被 sticker 刪除後的字串
        res = ""
        t_len = len(target)
        s_len = len(sticker)
        p1, p2 = 0, 0
        while p1 < t_len:
            if p2 == s_len:
                res += target[p1]
                p1 += 1
            else:
                if target[p1] == sticker[p2]:
                    p1 += 1
                    p2 += 1
                elif ord(target[p1]) > ord(sticker[p2]):
                    p2 += 1
                else: # ord(target[p1]) < ord(sticker[p2])
                    res += target[p1]
                    p1 += 1
        return res
    
    def sortString(self, s):
        return "".join(sorted(s))