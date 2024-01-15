# 二叉樹方案數：https://www.nowcoder.com/practice/aaefe5896cce4204b276e213e725f3ea
import sys

MAXN = 51
MOD = 1000000007
dp1 = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
dp2 = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
dp3 = [0] * MAXN

def main():
    input_buffer = sys.stdin.read().splitlines()

    line_index = 0
    while line_index < len(input_buffer):
        # n 個節點, 高度小於等於 m
        n, m = map(int, input_buffer[line_index].strip().split())
        line_index += 1

        # 輸出格式化
        sys.stdout.write(f"{compute1(n, m)}")


# 返回滿足 n 個節點同時高度小於等於 m 的方案數
def compute1(n: int, m: int) -> int:
    # base case
    if n == 0:
        return 1
    if m == 0:
        return 0
    # 查看記錄
    if dp1[n][m] != 0:
        return dp1[n][m]
    # 遞歸計算: k 為左子樹個數
    # n 個節點，head 佔 1
    ans = 0
    for k in range(n):
        ans = (ans + (compute1(k, m - 1) * compute1(n - k - 1, m - 1)) % MOD) % MOD

    dp1[n][m] = ans
    return ans

# 嚴格位置依賴
def compute2(n: int, m: int) -> int:
    for j in range(m+1):
        dp2[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 一共 i 個節點，head佔用1個
            # 若左樹佔用 k 個，右樹佔用 i - k - 1 個
            dp2[i][j] = 0
            for k in range(i):
                dp2[i][j] = (dp2[i][j] + (dp2[k][j-1] * dp2[i-k-1][j-1]) % MOD) % MOD
    
    return dp2[n][m]

# 嚴格位置依賴 + 狀態壓縮
def compute3(n: int, m: int) -> int:
    # Reset
    dp3[0] = 1
    for i in range(1, n+1):
        dp3[i] = 0

    for j in range(1, m+1):
        for i in range(n, 0, -1):
            dp3[i] = 0
            for k in range(i):
                dp3[i] = (dp3[i] + (dp3[k] * dp3[i-k-1]) % MOD) % MOD

    return dp3[n]


if __name__ == "__main__":
    main()