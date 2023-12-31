# 線段重合：https://www.nowcoder.com/practice/1ae8d0b6bb4e4bcdbf64ec491f63fc37
import sys
from heapq import *


def main():
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        n = int(input_buffer[line_index].strip())
        line_index += 1

        lines = []
        for _ in range(n):
            left, right = map(int, input_buffer[line_index].strip().split())
            line_index += 1
            lines.append([left, right])

        # 先按照左邊界排序
        lines.sort(key=lambda x: x[0])
        # 堆
        heap = []
        ans = 0
        for line in lines:
            # 若是小於等於左邊界的值，則彈出（代表影響不到此線段）
            while heap and heap[0] <= line[0]:
                heappop(heap)
            # 右邊界入堆
            heappush(heap, line[1])
            # 堆大小即為重合線段的數量
            size = len(heap)
            # 更新答案
            ans = max(ans, size)

        output_buffer.append(f'{ans}')


    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()