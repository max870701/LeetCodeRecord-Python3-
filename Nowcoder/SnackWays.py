# 牛牛的背包問題：https://www.nowcoder.com/practice/d94bb2fa461d42bcb4c0f2b94f5d4281
import sys

# arr[i...e]
# 返回值: ans 數組填到什麼位置（即長度）
def f(i, e, s, w, ans, j):
    global arr
    if s > w: return j
    # s <= w
    if i == e:
        ans.append(s)
        j += 1
    else:
        # s <= w 有兩種選擇
        # 不要 arr[i] 位置的數
        j = f(i+1, e, s, w, ans, j)
        # 要 arr[i] 位置的數
        j = f(i+1, e, s + arr[i], w, ans, j)

    return j

def main():
    global arr
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        n, w = map(int, input_buffer[line_index].strip().split())
        line_index += 1

        arr = list(map(int, input_buffer[line_index].strip().split()))
        line_index += 1

        lsum, rsum = [], []
        lsize = f(0, n >> 1, 0, w, lsum, 0)
        rsize = f(n >> 1, n, 0, w, rsum, 0)
        lsum.sort()
        rsum.sort()

        ans = 0
        right = 0
        for left in range(lsize-1, -1, -1):
            while right < rsize and lsum[left] + rsum[right] <= w:
                right += 1
            ans += right

        # 以下是另外一種雙指針解法：
        # left = 0
        # right = rsize - 1
        # while left < lsize and right >= 0:
        #     while lsum[left] + rsum[right] > w:
        #         right -= 1
        #     ans += right + 1
        #     left += 1

        output_buffer.append(f'{ans}')


    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()