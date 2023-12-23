class TrieNode:
    def __init__(self):
        self.pass_cnt = 0
        self.end_cnt = 0
        self.nexts = [None] * 26 # a-z : 0-26

# 固定數組實現
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        node.pass_cnt += 1
        for i in range(len(word)):
            char_index = ord(word[i]) - ord('a')
            if node.nexts[char_index] is None:
                node.nexts[char_index] = TrieNode()
            node = node.nexts[char_index]
            node.pass_cnt += 1
        node.end_cnt += 1

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            char_index = ord(word[i]) - ord('a')
            if node.nexts[char_index] is None: return False
            node = node.nexts[char_index]
        return node.end_cnt != 0

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            char_index = ord(prefix[i]) - ord('a')
            if node.nexts[char_index] is None: return False
            node = node.nexts[char_index]
        return True


# 哈希表實現
class Trie2:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        node.pass_cnt += 1
        for char in word:
            if char not in node.nexts:
                node.nexts.setdefault(char, TrieNode())
            node = node.nexts[char]
            node.pass_cnt += 1
        node.end_cnt += 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.nexts: return False
            node = node.nexts[char]
        return node.end_cnt != 0

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.nexts: return False
            node = node.nexts[char]
        return True
