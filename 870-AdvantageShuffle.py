class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 田忌賽馬
        n = len(nums2) # len(nums1) == len(nums2)
        # O(nlogn)
        # nums1 由小排到大
        nums1.sort()
        index = [i for i in range(n)]
        # O(nlogn)
        # 將 nums2 的 index 按照 value 由大排到小
        index.sort(key=lambda i:nums2[i], reverse=True)
        res = [0 for i in range(n)]
        for i in index:
            # Win
            if nums1[-1] > nums2[i]:
                res[i] = nums1.pop()
            # Lose
            else:
                res[i] = nums1.pop(0)
        return res            