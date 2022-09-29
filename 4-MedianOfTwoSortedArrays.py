class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new = nums1 + nums2
        new = sorted(new)
        l = len(new)
        mid = l // 2
        if l % 2 == 0:
            return float((new[mid-1] + new[mid])/2.0)
        else:
            return float(new[mid])