from collections import defaultdict
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.n = len(parents)
        self.dict = defaultdict(int)
        self.tree = self.buildTree(parents)
        self.countNodes(0)
        maxScore = max(self.dict.keys())
        
        return self.dict[maxScore]

    def buildTree(self, parents):
        tree = [[None] * 2 for _ in range(self.n)]
        for i in range(1, self.n):
            parent = parents[i]
            if not tree[parent][0]:
                tree[parent][0] = i
            else:
                tree[parent][1] = i
        return tree
    
    # 給定 root 根節點，計算節點數量
    def countNodes(self, root) -> int:
        if root is None: return 0

        left_cnt = self.countNodes(self.tree[root][0])
        right_cnt = self.countNodes(self.tree[root][1])
        # 後序
        root_cnt = left_cnt + right_cnt + 1
        res_cnt = self.n - root_cnt
        score = max(left_cnt, 1) * max(right_cnt, 1) * max(res_cnt, 1)
        self.dict[score] += 1

        return root_cnt