class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        # 26字母
        uf = UF(26)
        # 先處理 == 的字母
        for eq in equations:
            if eq[1] == "=":
                x = eq[0]
                y = eq[3]
                uf.union(ord(x) - ord('a'), ord(y) - ord('a'))
        # 再檢查不等關係
        for eq in equations:
            if eq[1] == "!":
                x = eq[0]
                y = eq[3]
                if uf.connected(ord(x) - ord('a'), ord(y) - ord('a')):
                    return False
        return True


class UF(object):
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP == rootQ:
            return
        
        self.parent[rootQ] = rootP
        self.count -= 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, p, q):
        return self.find(p) == self.find(q)