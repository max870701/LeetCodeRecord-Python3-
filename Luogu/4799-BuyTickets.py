# 世界冰球錦標賽：https://www.luogu.com.cn/problem/P4799
import sys

MAXN = 40
MAXM = 1 << 20

arr = [0 for _ in range(MAXN)]
lsum = [0 for _ in range(MAXM)]
rsum = [0 for _ in range(MAXM)]


def f(i, e, s, w, ans, j):
    if s > w: return j
    if i == e:
        ans[j] = s
        j += 1
    else:
        j = f(i+1, e, s, w, ans, j)
        j = f(i+1, e, s + arr[i], w, ans, j)

    return j

def main():
    input_buffer = sys.stdin.read().splitlines()
    output_buffer = []

    line_index = 0
    while line_index < len(input_buffer):
        n, w = map(int, input_buffer[line_index].strip().split())
        line_index += 1

        arr[:n] = list(map(int, input_buffer[line_index].strip().split()))
        line_index += 1

        lsize = f(0, n >> 1, 0, w, lsum, 0)
        rsize = f(n >> 1, n, 0, w, rsum, 0)
        lsum[:lsize] = sorted(lsum[:lsize])
        rsum[:rsize] = sorted(rsum[:rsize])

        ans = 0
        right = 0
        for left in range(lsize-1, -1, -1):
            while right < rsize and lsum[left] + rsum[right] <= w:
                right += 1
            ans += right

        output_buffer.append(f'{ans}')


    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()