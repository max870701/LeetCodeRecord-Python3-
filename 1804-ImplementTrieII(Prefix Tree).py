class TrieNode:
    # 節點資訊
    def __init__(self):
        self.pass_cnt = 0
        self.end_cnt = 0
        self.nexts = [None] * 26 # a - z : 0 - 25

# 固定數組實現 (類描述-動態結構)
class Trie:
    # 初始化根節點
    def __init__(self):
        self.root = TrieNode()

    # 將 word 加入節點
    def insert(self, word: str) -> None:
        node = self.root
        node.pass_cnt += 1
        for i in range(len(word)):
            char_index = ord(word[i]) - ord('a') # 減去 a 的 ascii 碼做偏移量
            if node.nexts[char_index] is None:
                node.nexts[char_index] = TrieNode()
            node = node.nexts[char_index]
            node.pass_cnt += 1
        node.end_cnt += 1

    # 計算 word 出現次數
    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for i in range(len(word)):
            char_index = ord(word[i]) - ord('a')
            if node.nexts[char_index] is None: # 斷掉說明沒出現過
                return 0
            node = node.nexts[char_index]
        
        return node.end_cnt

    # 計算 prefix 開頭的 string 數量
    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for i in range(len(prefix)):
            char_index = ord(prefix[i]) - ord('a')
            if node.nexts[char_index] is None:
                return 0
            node = node.nexts[char_index]

        return node.pass_cnt

    # 刪除 word
    # 情況1: 直接刪
    # 情況2: 剩一次，刪除額外分支
    def erase(self, word: str) -> None:
        if self.countWordsEqualTo(word):
            node = self.root
            node.pass_cnt -= 1
            for i in range(len(word)):
                char_index = ord(word[i]) - ord('a')
                if node.nexts[char_index].pass_cnt == 1:
                    node.nexts[char_index] = None
                    return
                node = node.nexts[char_index]
                node.pass_cnt -= 1
            node.end_cnt -= 1

# 哈希表實現 (類描述-動態結構)
class Trie2:
    # 初始化根節點
    def __init__(self):
        self.root = TrieNode()

    # 將 word 加入節點
    def insert(self, word: str) -> None:
        node = self.root
        node.pass_cnt += 1
        for char in word:
            if char not in node.nexts:
                node.nexts.setdefault(char, TrieNode())
            node = node.nexts[char]
            node.pass_cnt += 1
        node.end_cnt += 1

    # 計算 word 出現次數
    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.nexts: # 斷掉說明沒出現過
                return 0
            node = node.nexts[char]
        
        return node.end_cnt

    # 計算 prefix 開頭的 string 數量
    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.nexts:
                return 0
            node = node.nexts[char]

        return node.pass_cnt

    # 刪除 word
    # 情況1: 直接刪
    # 情況2: 剩一次，刪除額外分支
    def erase(self, word: str) -> None:
        if self.countWordsEqualTo(word):
            node = self.root
            node.pass_cnt -= 1
            for char in word:
                if node.nexts[char].pass_cnt == 1:
                    del node.nexts[char]
                    return
                node = node.nexts[char]
                node.pass_cnt -= 1
            node.end_cnt -= 1


# 靜態數組實現 (根據數據量估計需要的空間)
