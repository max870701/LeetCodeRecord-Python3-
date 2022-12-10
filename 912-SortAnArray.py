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