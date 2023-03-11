# You may have to add functionality to this data structure
# to solve the question. 

# For example, you could have to:
#   1. Add a BFS function to the Trie class to efficiently search
#     for "best"/longest word that was used to build the Trie 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Start with root
        cur = self.root
        # Loop over symbols in word
        for symbol in word:
            # Add symbol to cur.children
            # Update cur
            cur = cur.setdefault(symbol, TrieNode())
        # set cur.end to True
        cur.end = True

    def search_helper(self, word):
        # Start with root
        cur = self.root
        # Loop over all symbols in word
        for symbol in word:
            # Go to child of cur with matching symbol if exists
            if symbol in cur.children:
                cur = cur.children[symbol]
            # Else, return -1
            else:
                return -1
        # return 1 if cur.end else 0
        return 1 if cur.end else 0

    def search(self, word):
        # return helper == 1
        return self.search_helper(word) == 1

    def starts_with(self, prefix):
        # return helper >= 0
        return self.search_helper(prefix) >= 0
