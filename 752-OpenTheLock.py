from Queue import Queue
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # 記錄需要跳過的密碼
        deads = set(deadends)
        # 記錄已經窮舉過的密碼
        visited = set()
        # 佇列初始化
        q = Queue()
        # 起點
        step = 0
        q.put("0000")
        visited.add("0000")
        
        while not q.empty():
            sz = q.qsize()
            # 當前佇列中的所有節點向周圍擴散
            for _ in range(sz):
                cur = q.get()
                # 判斷是否到達終點
                if cur in deads: continue
                if cur == target:
                    return step
                # 將一個節點的未遍歷相鄰節點加入佇列
                for j in range(4):
                    up = self.plusOne(cur, j)
                    if up not in visited:
                        q.put(up)
                        visited.add(up)
                    down = self.minusOne(cur, j)
                    if down not in visited:
                        q.put(down)
                        visited.add(down)
            step += 1
        # 沒找到
        return -1

    def plusOne(self, s, j):
        if s[j] == "9":
            n = 0
        else:
            n = int(s[j]) + 1
        return s[:j] + str(n) + s[j+1:]

    def minusOne(self, s, j):
        if s[j] == "0":
            n = 9
        else:
            n = int(s[j]) - 1
        return s[:j] + str(n) + s[j+1:]
        