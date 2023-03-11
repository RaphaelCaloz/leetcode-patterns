class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Start with root
        # Loop over symbols in word
            # Add symbol to curr.children
            # Update curr
        # set curr.end to True

    def search_helper(self, word):
        # Start with root
        # Loop over all symbols in word
            # Go to child of curr with matching symbol if exists
            # Else, return -1
        # return 1 if curr.end else 0 

    def search(self, word):
        # return helper == 1

    def starts_with(self, prefix):
        # return helper >= 0

