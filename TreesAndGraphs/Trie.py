class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        temp = self.root
        for i in range(len(word)):
            letter = word[i].lower()
            if letter not in temp.children:
                temp.children[letter] = TrieNode()

            temp = temp.children[letter]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        searchBranchQueue = [(self.root,0)]
        i = 0

        while searchBranchQueue and i < len(word):
            letter = word[i].lower()

            if letter == '.':
                for node in searchBranchQueue[0][0].children:
                    searchBranchQueue.append((searchBranchQueue[0][0].children[node],i+1))
            elif letter in searchBranchQueue[0][0].children:
                searchBranchQueue.append((searchBranchQueue[0][0].children[letter], i + 1))

            searchBranchQueue.pop(0)
            if searchBranchQueue:
                i = searchBranchQueue[0][1]

        if searchBranchQueue:
            return True
        else:
            return False