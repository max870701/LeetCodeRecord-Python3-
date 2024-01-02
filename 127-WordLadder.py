# 雙向 BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set: return 0
        smallLevel, bigLevel, nextLevel = set(), set(), set()
        smallLevel.add(beginWord)
        bigLevel.add(endWord)
        levels = 2
        # 若小側還有路徑
        while len(smallLevel):
            # 從小側開始擴展
            for word in smallLevel:
                word_size = len(word)
                # 每一位替換
                for replaced_pos in range(word_size):
                    # 遍歷 a-z 
                    for n in range(ord('a'), ord('z')+1):
                        if chr(n) == word[replaced_pos]: continue
                        new_word = self.replaceString(word, replaced_pos, chr(n))
                        # 若存在大側邊集合中（路徑連通），返回結果
                        if new_word in bigLevel:
                            return levels
                        if new_word in word_set:
                            # 剪枝去重
                            word_set.remove(new_word)
                            # 加到下一階層
                            nextLevel.add(new_word)

            if len(nextLevel) <= len(bigLevel):
                smallLevel, nextLevel = nextLevel, smallLevel
            else: # len(nextLevel) > len(bigLevel)
                smallLevel, bigLevel, nextLevel = bigLevel, nextLevel, smallLevel
            nextLevel.clear()
            levels += 1
        return 0

    def replaceString(self, string, i, char):
        n = len(string)
        if i == 0:
            return char + string[1:]
        elif i == n-1:
            return string[:n-1] + char
        else:
            return string[:i] + char + string[i+1:]