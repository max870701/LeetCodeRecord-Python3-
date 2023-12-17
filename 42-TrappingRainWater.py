class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        zeros = [0] * (n-1)
        l_max = [height[0]] + zeros
        for i in range(1, n):
            l_max[i] = max(l_max[i-1], height[i])

        r_max = zeros + [height[n-1]]
        for i in range(n-2, -1, -1):
            r_max[i] = max(r_max[i+1], height[i])

        ans = 0
        for i in range(1, n-1):
            ans += max(0, min(l_max[i], r_max[i]) - height[i])

        return ans