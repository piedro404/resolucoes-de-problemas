class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def count_keystrokes(self, word):
        node = self.root
        keystrokes = 1
        for i in range(1, len(word)):
            node = node.children[word[i-1]]
            if node.count > 1:
                keystrokes += 1
        return keystrokes