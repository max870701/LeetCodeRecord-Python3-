class Solution:
    def __init__(self):
        MAXN = 100001
        self.father = list(range(MAXN))
        self.secret = list(range(MAXN))

    def build(self, n, firstPerson):
        self.father[:n] = [i for i in range(n)]
        self.secret[:n] = [False for _ in range(n)]
        self.father[firstPerson] = 0
        self.secret[0] = True

    def find(self, e):
        if e != self.father[e]:
            self.father[e] = self.find(self.father[e])
        return self.father[e]
    
    def union(self, a, b):
        a_f, b_f = self.find(a), self.find(b)
        if a_f != b_f:
            self.father[a_f] = b_f
            self.secret[b_f] = self.secret[b_f] or self.secret[a_f]

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        self.build(n, firstPerson)
        # 會議排序
        meetings.sort(key=lambda m: m[2])
        m = len(meetings)
        # 遍歷會議
        l = 0
        while l < m:
            r = l
            # [l...r] 範圍屬於同一時間舉行的會議
            while (r+1 < m )and meetings[l][2] == meetings[r+1][2]:
                r += 1
            # 合併知道和不知道秘密的人
            for i in range(l, r+1):
                self.union(meetings[i][0], meetings[i][1])
            # 撤銷
            for j in range(l, r+1):
                person1, person2 = meetings[j][0], meetings[j][1]
                p1_f, p2_f = self.find(person1), self.find(person2)
                if not self.secret[p1_f]:
                    self.father[person1] = person1
                if not self.secret[p2_f]:
                    self.father[person2] = person2
            # 迭代會議
            l = r + 1
        # 收集
        return [i for i in range(n) if self.secret[self.find(i)]]