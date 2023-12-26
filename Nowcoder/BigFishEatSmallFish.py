# 大魚吃小魚：https://www.nowcoder.com/practice/77199defc4b74b24b8ebf6244e1793de
import sys

MAXN = 100001
arr = [0] * MAXN
stack = [[0, 0] for _ in range(MAXN)] # 記錄魚的大小和所需輪數

def main():
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        # n 條魚
        n = int(input_buffer[line_index])
        line_index += 1
        # 魚體重序列，轉為 list
        values = list(map(int, input_buffer[line_index].strip().split()))
        line_index += 1

        # 直接將值賦給 arr，避免不必要的列表操作
        arr[:n] = values
        ans = compute(n, arr, stack)  # 將必要的變量作為參數傳遞
        # 輸出格式化
        output_buffer.extend(f"{ans}")

    sys.stdout.write("\n".join(output_buffer))

# arr[0 .. n-1] 代表魚的體重
# stack 為單調棧
def compute(n, arr, stack):
    r = 0
    ans = 0
    # 反向遍歷: 棧底小-棧頂大
    for i in range(n-1, -1, -1):
        curTurns = 0
        # 彈出
        while r > 0 and arr[i] > stack[r-1][0]:
            curTurns = max(curTurns + 1, stack[r-1][1])
            r -= 1
        # 壓棧
        stack[r][0] = arr[i]
        stack[r][1] = curTurns
        r += 1
        ans = max(ans, curTurns)
    return ans


if __name__ == "__main__":
    main()
