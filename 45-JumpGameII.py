class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        window_left = 0
        window_right = 0

        # Break the while loop when reaching the last position
        while window_right < len(nums) - 1:
            farthest = 0
            # Iterate all elements in a window
            for i in range(window_left, window_right + 1):
                farthest = max(farthest, i + nums[i])
            
            window_left = window_right + 1
            window_right = farthest
            ans += 1
        
        return ans