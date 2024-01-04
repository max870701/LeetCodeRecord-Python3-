# 飛行路線：https://www.luogu.com.cn/problem/P4568
import sys
from heapq import *

MAXN = 10001   # 城市數量
MAXM = 100001  # 航線數量
MAXK = 11      # 免單次數

# 鏈式前向星
head = [-1] * MAXN
next = [-1] * MAXM
to = [0] * MAXM
weight = [0] * MAXM
cnt = 1

# Dijkstra
distance = [[float('inf')] * MAXK for _ in range(MAXN)]
visited = [[False] * MAXK for _ in range(MAXN)]
heap = []

def addEdge(u, v, w):
    global cnt
    to[cnt] = v
    weight[cnt] = w
    next[cnt] = head[u]
    head[u] = cnt
    cnt += 1

def dijkstra(s, t, k):
    distance[s][0] = 0
    # (沿途花費, 到達的城市編號, 已使用的免單次數)
    heappush(heap, (0, s, 0))
    while heap:
        cost, cur, quota = heappop(heap)
        if visited[cur][quota]: continue
        visited[cur][quota] = True
        if cur == t:
            return cost

        i_edge = head[cur]
        while i_edge != -1:
            to_node, w = to[i_edge], weight[i_edge]
            # 使用免費額度
            if quota < k and distance[to_node][quota+1] > distance[cur][quota]:
                distance[to_node][quota+1] = distance[cur][quota]
                heappush(heap, (distance[to_node][quota+1], to_node, quota+1))
            # 不使用免費額度
            if distance[to_node][quota] > distance[cur][quota] + w:
                distance[to_node][quota] = distance[cur][quota] + w
                heappush(heap, (distance[to_node][quota], to_node, quota))
            i_edge = next[i_edge]
    return -1

def main():
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        n, m, k = map(int, input_buffer[line_index].strip().split())
        line_index += 1

        s, t = map(int, input_buffer[line_index].strip().split())
        line_index += 1
        
        # 鏈式前向星建圖
        for _ in range(m):
            from_node, to_node, dis = map(int, input_buffer[line_index].strip().split())
            line_index += 1
            addEdge(from_node, to_node, dis)
            addEdge(to_node, from_node, dis)

        output_buffer.append(str(dijkstra(s, t, k)))

    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()