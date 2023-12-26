class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mergeSort(nums, 0, len(nums)-1)
        return nums

    def mergeSort(self, li, lo, hi):
        if lo < hi:
            mid = (lo + hi) // 2
            # sort the left part of the array
            self.mergeSort(li, lo, mid)
            # sort the right part of the array
            self.mergeSort(li, mid+1, hi)
            #postorder
            self.merge(li, lo, mid, hi)

    def merge(self, li, lo, mid, hi):
        # Two pointer skill
        i = lo
        j = mid + 1
        tmp = []
        while i <= mid and j <= hi:
            if li[i] < li[j]:
                tmp.append(li[i])
                i += 1
            else: # li[i] > li[j]
                tmp.append(li[j])
                j += 1
        if i <= mid:
            tmp += li[i:mid+1]
        if j <= hi:
            tmp += li[j:hi+1]
            
        li[lo:hi+1] = tmp


class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.help = [None] * n
        self.nums = nums
        self.mergeSort(0, n-1)
        return nums

    # [left, right] 索引範圍上排序
    def mergeSort(self, left, right):
        if left == right: return
        
        mid = (left + right) // 2

        self.mergeSort(left, mid)
        self.mergeSort(mid+1, right)
        self.merge(left, mid, right)

    # 合併 [left, mid], [mid+1, right] 兩數組
    def merge(self, left, mid, right):
        i = left
        p1 = left
        p2 = mid + 1

        while p1 <= mid and p2 <= right:
            if self.nums[p1] <= self.nums[p2]:
                self.help[i] = self.nums[p1]
                p1 += 1
            else:
                self.help[i] = self.nums[p2]
                p2 += 1
            i += 1
            
        while p1 <= mid: # p2 越界
            self.help[i] = self.nums[p1]
            i += 1
            p1 += 1
        while p2 <= right: # p1 越界
            self.help[i] = self.nums[p2]
            i += 1
            p2 += 1
        for k in range(left, right+1):
            self.nums[k] = self.help[k]
    
class Solution3:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.n = len(nums)
        self.help = [None] * self.n
        self.nums = nums
        self.mergeSort()
        return nums

    # [left, right] 索引範圍上排序
    # 迴圈版
    def mergeSort(self):
        step = 1
        while step < self.n:
            left = 0
            while left < self.n:
                mid = left + step - 1
                if mid + 1 >= self.n: break
                right = min(self.n-1, left + 2*step -1)
                self.merge(left, mid, right)
                left = right + 1
            step *= 2

    # 合併 [left, mid], [mid+1, right] 兩數組
    def merge(self, left, mid, right):
        i = left
        p1 = left
        p2 = mid + 1

        while p1 <= mid and p2 <= right:
            if self.nums[p1] <= self.nums[p2]:
                self.help[i] = self.nums[p1]
                p1 += 1
            else:
                self.help[i] = self.nums[p2]
                p2 += 1
            i += 1
            
        while p1 <= mid: # p2 越界
            self.help[i] = self.nums[p1]
            i += 1
            p1 += 1
        while p2 <= right: # p1 越界
            self.help[i] = self.nums[p2]
            i += 1
            p2 += 1
        for k in range(left, right+1):
            self.nums[k] = self.help[k]