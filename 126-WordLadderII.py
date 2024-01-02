class Solution:
    def build(self, wordList):
        self.dict = set(wordList)
        self.currentLevel = set()
        self.nextLevel = set()
        self.graph = dict() # key: str, value: list
        self.path = [] # List[str]
        self.ans = [] # List[List[str]]

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.build(wordList)
        if endWord not in self.dict:
            return self.ans
        if self.bfs(beginWord, endWord):
            # 反圖查找
            self.dfs(endWord, beginWord)
        return self.ans
    
    def bfs(self, beginWord, endWord):
        find = False
        self.currentLevel.add(beginWord)
        # 層序遍歷
        while len(self.currentLevel):
            # difference update 方法: Removes the items in this set that are also included in a specified set.
            # 相減運算也有一樣效果
            self.dict.difference_update(self.currentLevel)
            for word in self.currentLevel:
                # word 去擴，每一位 a-z 去換，且避免加工出自身字符
                word_size = len(word)
                for replaced_pos in range(word_size):
                    for n in range(ord('a'), ord('z')+1):
                        new_string = self.replaceStr(word, replaced_pos, chr(n))
                        if new_string != word and new_string in self.dict:
                            if new_string == endWord:
                                find = True
                            self.graph.setdefault(new_string, [])
                            self.graph[new_string].append(word)
                            self.nextLevel.add(new_string)
            if find:
                return True
            else:
                self.currentLevel, self.nextLevel = self.nextLevel, self.currentLevel
                self.nextLevel.clear()

        return False
                    
    def replaceStr(self, string, i, char):
        n = len(string)
        if i == 0:
            return char + string[1:]
        elif i == n-1:
            return string[:n-1] + char
        else:
            return string[:i] + char + string[i+1:]

    def dfs(self, word, target):
        self.path.insert(0, word)
        if word == target:
            self.ans.append(self.path[:])
        elif word in self.graph:
            for n in self.graph[word]:
                self.dfs(n, target)
        self.path.pop(0)