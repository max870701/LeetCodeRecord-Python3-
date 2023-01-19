def knapsack(W, N, wt, value):
    """
    給定一個可裝載容量為 W 的背包和 N 個物品，每個物品有重量和價值兩個屬性。
    其中第 i 個物品的重量為 wt[i]，價值為 val[i]，現在讓你用這個背包裝物品，最多能裝的價值是多少
    :type W: int
    :type N: int
    :type wt: list
    :type value: list
    :rtype: int
    """
    # 定義 dp 數組並初始化
    dp =[[0 for _ in range(N+1)] for _ in range(W+1)]
    # 進行狀態轉移
    # wt 和 value 存在索引偏移
    for i in range(1, N+1):
        for w in range(1, W+1):
            # 第 i 個物品直接超出背包可裝載量
            if w - wt[i-1] > 0:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(
                    # 不選第 i 個
                    dp[i-1][w],
                    # 選第 i 個，重量為 wt[i-1]
                    value[i-1] + dp[i-1][w - wt[i-1]]
                )
    return dp[N][W]

