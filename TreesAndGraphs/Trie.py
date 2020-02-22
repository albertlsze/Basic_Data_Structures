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
        searchBranch = [self.root]
        searchOutput = [True]
        for i in range(len(word)):
            newBranches = []
            newOutput = []
            for branch in range(0, len(searchBranch)):
                if not searchOutput[branch]:
                    continue
                if word[i] == '.':
                    if len(searchBranch[branch].children.keys()) < 1:
                        searchOutput[branch] = False
                    else:
                        for key in searchBranch[branch].children:
                            newBranches.append(searchBranch[branch].children[key])
                            newOutput.append(True)

                letter = word[i].lower()
                if letter in searchBranch[branch].children:
                    searchBranch[branch] = searchBranch[branch].children[letter]
                else:
                    searchOutput[branch] = False

            if len(newBranches) > 0:
                searchBranch = newBranches
                searchOutput = newOutput

        return True in searchOutput