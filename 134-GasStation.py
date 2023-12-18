class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # res_gas = gas - cost
        n = len(gas)
        # 嘗試從 0 ~ n-1 出發
        # l為窗口左側，出發位置
        # r 為窗口右側
        # gas_sum 為當前油量累加和
        # window 為窗口大小
        window = 0
        gas_sum = 0
        r = 0
        for l in range(n):
            while gas_sum >= 0:
                if window == n:
                    return l
                # r 為窗口右移的 index（環形），從 l 開始加上窗口長度再取模
                r = (l + window) % n 
                # 更新 window 大小
                window += 1
                # 更新油量累加和
                gas_sum += gas[r] - cost[r]
                
            # gas_sum < 0，則代表從 l 出發無法完成一圈， 那麼左側窗口收緊
            window -= 1
            # 左側窗口收緊後，gas_sum 要剪去 l 位置的累加和
            gas_sum -= gas[l] - cost[l]
        return -1