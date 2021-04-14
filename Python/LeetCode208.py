class treeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = dict()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = treeNode(True)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for ch in word:
            if ch not in p.children:
                p.children[ch] = treeNode(False)
            p = p.children[ch]
        p.val = True
        return 

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for ch in word:
            if ch not in p.children:
                return False
            p = p.children[ch]
        return p.val

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for ch in prefix:
            if ch not in p.children:
                return False
            p = p.children[ch]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)