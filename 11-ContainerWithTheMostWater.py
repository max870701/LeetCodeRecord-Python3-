class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans
    
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_store = 0
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            max_store = max(area, max_store)

            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1

        return max_store