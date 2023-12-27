# 並查集實現：https://www.nowcoder.com/practice/e7ed657974934a30b2010046536a5372
class UnionFind:
    def __init__(self, n):
        # 記錄父節點
        self.father = [i for i in range(n)]
        # 記錄集合大小
        self.size = [1 for _ in range(n)]
    
    # 查詢 e 元素所在集合的代表元素 (父元素)
    def find(self, e):
        stack = []
        # 查找父元素
        while e != self.father[e]:
            stack.append(e)
            e = self.father[self.father[e]]
        
        # 扁平化優化
        while stack:
            cur = stack.pop()
            self.father[cur] = e
        return e

    # 查詢 a, b 兩元素所在的集合是否相等 (即相同父元素)
    def isSameSet(self, a, b):
        return self.find(a) == self.find(b)
    
    # 合併 a, b 兩元素所在集合
    def union(self, a, b):
        a_father = self.find(a)
        b_father = self.find(b)
        # father 不同才合併，依照小褂大進行合併 
        if a_father != b_father:
            # 小掛大
            if self.size[a_father] <= self.size[b_father]:
                self.father[a_father] = b_father
                self.size[b_father] += self.size[a_father]
            else:
                self.father[b_father] = a_father
                self.size[a_father] += self.size[b_father]