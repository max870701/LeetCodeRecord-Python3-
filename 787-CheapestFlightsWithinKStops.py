# Bellmon-Ford 算法
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cur_dis = [float('inf')] * n
        cur_dis[src] = 0
        for _ in range(k+1):
            next_dis = cur_dis[:]
            for edge in flights:
                from_node, to_node, price = edge
                if cur_dis[from_node] != float('inf'):
                    # 鬆弛過程
                    next_dis[to_node] = min(next_dis[to_node], cur_dis[from_node] + price)
            # 進到下一輪
            cur_dis = next_dis
        
        return -1 if cur_dis[dst] == float('inf') else cur_dis[dst]