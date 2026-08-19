class TrieNode():

    def __init__(self):
        self.child = {}
        self.end = False
    
class Trie():
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, w):
        curr = self.root
        for c in w:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.end = True
    
    def search(self, w):
        curr = self.root
        for c in w:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.end

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        trie = Trie()
        for w in dictionary:
            trie.insert(w)

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 0

            res = 1 + dfs(i + 1)

            for w in dictionary:
                len_w = len(w)
                if trie.search(s[i: i + len_w]):
                    res = min(res, dfs(i + len_w))
            memo[i] = res
            return res
        
        
        return dfs(0)








        
        