class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 單調棧：棧底大，棧頂小
        mono_stack = []
        r = 0
        n = len(nums2)
        ans = dict()
        # 遍歷
        for i in range(n):
            # 彈出規則
            while r > 0 and nums2[mono_stack[r-1]] < nums2[i]:
                cur = mono_stack.pop()
                r -= 1
                ans.setdefault(nums2[cur], nums2[i])
            # 壓棧
            mono_stack.append(i)
            r += 1

        # 清算
        while r > 0:
            cur = mono_stack.pop()
            r -= 1
            ans.setdefault(nums2[cur], -1)

        return [ans[i] for i in nums1]