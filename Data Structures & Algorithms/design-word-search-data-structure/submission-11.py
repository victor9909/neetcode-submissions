class Node():

    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.end = True

    def search(self, word: str) -> bool:

        curr = self.root
        def dfs(curr, i):

            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for c in curr.child:
                        if dfs(curr.child[c], j + 1):
                            return True
                    return False
                else:
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]
            
            return curr.end
        
        return dfs(curr, 0)
            


        
