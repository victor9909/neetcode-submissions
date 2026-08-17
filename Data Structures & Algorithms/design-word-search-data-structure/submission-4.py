class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.word_dict = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.word_dict
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(root, i):
            
            curr = root

            for j in range(i, len(word)):
                c = word[j]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(child, j + 1):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end
        
        return dfs(self.word_dict, 0)
        

        









