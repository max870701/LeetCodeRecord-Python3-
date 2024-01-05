# Clear And Present Danger S：https://www.luogu.com.cn/problem/P2910
import sys

MAXN = 101
MAXM = 10001
# 鄰接矩陣圖
distance = [[float('inf') for _ in range(MAXN)]for _ in range(MAXN)]
# 目標路徑
path = [0 for _ in range(MAXM)]

def main():
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        # n 個節點, m 條邊
        n, m = map(int, input_buffer[line_index].strip().split())
        line_index += 1
        # 加入路徑
        for i in range(m):
            node = int(input_buffer[line_index].strip())
            line_index += 1
            path[i] = node - 1
        # 遍歷鄰接矩陣，更新距離值
        for i in range(n):
            row = list(map(int, input_buffer[line_index].strip().split()))
            line_index += 1
            for j in range(n):
                distance[i][j] = row[j]
        # Floyd算法 -> 得出任意兩點的最短路徑
        for bridge in range(n):
            for i in range(n):
                for j in range(n):
                    if (distance[i][bridge] != float('inf')) and (distance[bridge][j] != float('inf')) \
                    and (distance[i][j] > distance[i][bridge] + distance[bridge][j]):
                        distance[i][j] = distance[i][bridge] + distance[bridge][j]
        # 按照 Path 計算答案
        ans = 0
        for i in range(1, m):
            ans += distance[path[i-1]][path[i]]
         
        output_buffer.append(f"{ans}")


    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()