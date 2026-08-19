class TrieNode():

    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.end = True

    def search(self, word: str) -> bool:

        curr = self.root

        def dfs(i, node):

            if i >= len(word):
                return node.end
            
            if word[i] == ".":
                for child in node.child.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if word[i] in node.child:
                    node = node.child[word[i]]
                    return dfs(i + 1, node)
                else:
                    return False
        
        return dfs(0, curr)





        
