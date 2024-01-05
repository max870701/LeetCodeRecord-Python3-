# Bellman-Ford + SPFA(Ahortest Path Faster Algorithm) + Negative Cycle Judgement
# 負環：https://www.luogu.com.cn/problem/P3385
import sys

MAXN = 2001
MAXM = 6001

head = [-1] * MAXN
next = [-1] * MAXM
to = [0] * MAXM
weight = [0] * MAXM
cnt = 1

MAXQ = 4000001
distance = [0] * MAXN
updateCnt = [0] * MAXN
queue = [0] * MAXQ
l = 0
r = -1
enter = [False] * MAXN

def addEdge(u, v, w):
    global cnt, head, next, to, weight
    next[cnt] = head[u]
    to[cnt] = v
    weight[cnt] = w
    head[u] = cnt
    cnt += 1

def build(n):
    global cnt, l, r, head, enter, distance, updateCnt
    cnt = 1
    l = 0
    r = -1
    head[:n+1] = [-1] * (n + 1)
    enter[:n+1] = [False] * (n + 1)
    distance[:n+1] = [float('inf')] * (n + 1)
    updateCnt[:n+1] = [0] * (n + 1)

def spfa(n):
    global l, r, queue, enter, distance, updateCnt, head, to, weight
    distance[1] = 0
    updateCnt[1] += 1
    r += 1
    queue[r % MAXQ] = 1
    enter[1] = True
    while l <= r:
        from_node = queue[l % MAXQ]
        l += 1
        enter[from_node] = False
        edge_i = head[from_node]
        while edge_i != -1:
            to_node = to[edge_i]
            w = weight[edge_i]
            if distance[from_node] + w < distance[to_node]:
                distance[to_node] = distance[from_node] + w
                if not enter[to_node]:
                    if updateCnt[to_node] == n:
                        return True
                    updateCnt[to_node] += 1
                    r += 1
                    queue[r % MAXQ] = to_node
                    enter[to_node] = True
            edge_i = next[edge_i]
    return False

def main():
    global n, m
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    cases = int(input_buffer[line_index].strip())
    line_index += 1
    for _ in range(cases):
        n, m = map(int, input_buffer[line_index].strip().split())
        line_index += 1
        build(n)
        for _ in range(m):
            from_node, to_node, dis = map(int, input_buffer[line_index].strip().split())
            line_index += 1
            if dis >= 0:
                addEdge(from_node, to_node, dis)
                addEdge(to_node, from_node, dis)
            else:
                addEdge(from_node, to_node, dis)
        output_buffer.append("YES" if spfa(n) else "NO")

    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()