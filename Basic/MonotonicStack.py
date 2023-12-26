# 單調棧結構：https://www.nowcoder.com/practice/2a2c00e7a88a498693568cef63a4b7bb
import sys

MAXN = 1000001
arr = [0] * MAXN
stack = [0] * MAXN
ans = [[-1, -1] for _ in range(MAXN)]

def main():
    """
    主函數，從標準輸入讀取數據並計算結果，將結果寫入標準輸出。

    輸入格式：
    第一行包含一個整數 n，表示數組的長度。
    第二行包含 n 個整數，表示數組的元素。

    輸出格式：
    對於每個元素，輸出兩個整數，表示該元素的計算結果。

    範例：
    輸入：
    7
    3 4 1 5 6 2 7
    輸出：
    -1 2
    0 2
    -1 -1
    2 5
    3 5
    2 -1
    5 -1
    """
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        n = int(input_buffer[line_index])
        line_index += 1
        values = list(map(int, input_buffer[line_index].strip().split()))
        line_index += 1

        # 直接將值賦給 arr，避免不必要的列表操作
        arr[:n] = values
        compute(n, arr, stack, ans)  # 將必要的變量作為參數傳遞
        # 使用列表推導式進行輸出格式化，通常更快
        output_buffer.extend(f"{ans[i][0]} {ans[i][1]}" for i in range(n))

    sys.stdout.write('\n'.join(output_buffer))

# arr [0, n-1]
def compute(n, arr, stack, ans):
    r = 0
    # 遍歷階段
    for i in range(n):
        while r > 0 and arr[stack[r - 1]] >= arr[i]:
            cur = stack[r - 1] # 彈出當前 stack 棧頂位置的 index
            r -= 1
            # 彈出就記錄答案
            # 左邊比 cur 索引值小的索引
            ans[cur][0] = stack[r - 1] if r > 0 else -1
            # 右邊比 cur 索引值小的索引
            ans[cur][1] = i

        stack[r] = i
        r += 1

    # 清算階段: 棧裡還有元素
    while r > 0:
        cur = stack[r - 1]
        r -= 1
        ans[cur][0] = stack[r - 1] if r > 0 else -1
        ans[cur][1] = -1
    # 修正階段: 左側答案一定是對的，右側答案可能出現索引對應值與當前索引對應值相等
    # 最後一個元素的右側答案必為 -1，可跳過
    for i in range(n - 2, -1, -1):
        if ans[i][1] != -1 and arr[ans[i][1]] == arr[i]:
            ans[i][1] = ans[ans[i][1]][1]

if __name__ == "__main__":
    main()