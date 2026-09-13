# Session 1, attempt 2: neetcode video

class trieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = trieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        # this is such a sick fuckign for loop
        for ltr in word:
            if ltr not in curr.children:
                curr.children[ltr] = trieNode()
            curr = curr.children[ltr]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ltr in word:
            if ltr not in curr.children:
                return False
            curr = curr.children[ltr]

        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ltr in prefix:
            if ltr not in curr.children:
                return False
            curr = curr.children[ltr]
        
        return True
        
        