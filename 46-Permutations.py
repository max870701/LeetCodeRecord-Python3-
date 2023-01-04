class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        track = []
        self.backtrack(nums, track)
        return self.res
    
    def backtrack(self, nums, track):
        """
        :type nums: List[int]
        :type track: 
        :rtype:
        """
        # 到達葉子節點，將路徑裝入結果列表
        if len(track) == len(nums):
            self.res.append(list(track))
            return

        for i in range(len(nums)):
            # 排除不合法的選擇
            if nums[i] in track: continue
            # 做選擇
            track.append(nums[i])
            # 進入下一層決策樹
            self.backtrack(nums, track)
            # 取消選擇
            track.pop()

    
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.track = []
        self.backtrack(nums)
        return self.res
    
    def backtrack1self, nums):
        """
        :type nums: List[int]
        :type track: 
        :rtype:
        """
        # 到達葉子節點，將路徑裝入結果列表
        if len(self.track) == len(nums):
            self.res.append(list(self.track))
            return

        for i in range(len(nums)):
            # 排除不合法的選擇
            if nums[i] in self.track: continue
            # 做選擇
            self.track.append(nums[i])
            # 進入下一層決策樹
            self.backtrack(nums)
            # 取消選擇
            self.track.pop()