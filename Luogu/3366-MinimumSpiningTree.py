# 最小生成樹：https://www.luogu.com.cn/problem/P3366
import sys

def find(e):
    global father
    if e != father[e]:
        father[e] = find(father[e])
    return father[e]

def union(a, b):
    global father
    a_f, b_f = find(a), find(b)
    # 不在同一集合，可合併
    if a_f != b_f:
        father[a_f] = b_f
        return True
    # 若已經在同一集合，意味著會形成環
    else:
        return False

def main():
    global father
    global edges
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        # n 為節點數量, m 為邊的數量
        n, m = map(int, input_buffer[line_index].strip().split())
        line_index += 1
        # 建立 father
        father = [i for i in range(n+1)]

        # edges 收集
        edges = [[0]*3 for _ in range(m)]
        for i in range(m):
            node1, node2, weight = map(int, input_buffer[line_index].strip().split())
            line_index += 1
            edges[i][0] = node1
            edges[i][1] = node2
            edges[i][2] = weight
        
        # edges 照權重排序
        edges = sorted(edges, key=lambda x: x[2])
        # 遍歷生成最小生成樹
        ans = 0
        edgeCnt = 0
        for edge in edges:
            if union(edge[0], edge[1]):
                edgeCnt += 1
                ans += edge[2]
         
        output_buffer.append(str(ans) if edgeCnt == n-1 else "orz")


    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()