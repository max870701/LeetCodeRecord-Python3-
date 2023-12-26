class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1000000007
        n = len(arr)
        mono_stack = []
        r = 0
        ans = 0
        # 遍歷階段
        for i in range(n):
            # 彈出
            while r > 0 and arr[i] <= arr[mono_stack[r-1]]:
                cur = mono_stack.pop()
                r -= 1
                left = mono_stack[r-1] if r > 0 else -1
                # left-cur, cur-right, min value
                ans = (ans + (cur - left) * (i - cur) * (arr[cur])) % MOD
            # 壓入
            mono_stack.append(i)
            r += 1
        # 清算
        while r > 0:
            cur = mono_stack.pop()
            r -= 1
            left = mono_stack[r-1] if r > 0 else -1
            ans = (ans + (cur - left) * (n - cur) * (arr[cur])) % MOD
        
        return ans