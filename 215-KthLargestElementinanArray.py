class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)-1
        k = len(nums) - k
        while l < r:
            pivot_index = self.partition(nums, l, r)
            if pivot_index == k:
                break
            elif pivot_index > k:
                r = pivot_index - 1
            elif pivot_index < k:
                l = pivot_index + 1

        return nums[k]
    

    def partition(self, arr, l, r):
        pivot = arr[r]
        i = l-1
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[r], arr[i+1] = arr[i+1], arr[r]

        return i+1