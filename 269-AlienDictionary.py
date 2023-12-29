class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 入度表初始化
        n = 26
        indegree = [-1] * n
        for word in words:
            for char in word:
                indegree[ord(char)-ord('a')] = 0
        # 建圖
        graph = [[] for _ in range(n)]
        for i in range(len(words)-1):
            cur_word, next_word = words[i], words[i+1]
            min_len = min(len(cur_word), len(next_word))
            for j in range(min_len):
                cur_char, next_char = cur_word[j], next_word[j]
                if cur_char != next_char:
                    graph[ord(cur_char)-ord('a')].append(ord(next_char) - ord('a'))
                    indegree[ord(next_char)-ord('a')] += 1
                    break
            if len(cur_word) > len(next_word) and cur_word[:min_len] == next_word[:min_len]:
                return ""
        # 拓墣排序
        queue = list(range(n))
        l, r = 0, 0
        kinds = 0
        for i in range(n):
            if indegree[i] != -1:
                kinds += 1
            if indegree[i] == 0:
                queue[r] = i
                r += 1
        ans = ""
        while l < r:
            cur_node = queue[l]
            l += 1
            ans += chr(cur_node + ord('a'))
            for char_n in graph[cur_node]:
                indegree[char_n] -= 1
                if indegree[char_n] == 0:
                    queue[r] = char_n
                    r += 1

        return ans if len(ans) == kinds else "" 