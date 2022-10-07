class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # two hash map
        res = []
        dict1, dict2 = self.generate_dict(l=nums1), self.generate_dict(l=nums2)
        
        for key, value in dict1.items():
            if key in dict2:
                amount = min(value, dict2[key])
                for n in range(amount):
                    res.append(key)

        return res

    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # one hash map
        # Time O(n+m)
        # Space O(min(n, m))
        res = []
        count = 0
        dict1 = self.generate_dict(l=nums1)
        
        for num in nums2:
            if dict1[num]:
                res.append(num)
                dict1[num] -= 1

        return res

    def generate_dict(self, l):
        tmp = collections.defaultdict(int)
        for n in l:
            tmp[n] += 1
        return tmp

    def intersect3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # sort
        # n is the lengths of nums1, m is the lengths of nums2
        # Time O(nlogn + mlogm)
        # Space from O(logn + logm) to O(n+m)
        res = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0

        while i < nums1_len and j < nums2_len:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else: # nums1[i] < nums2[j]
                i += 1

        return res