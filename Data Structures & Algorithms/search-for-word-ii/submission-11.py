class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        class Node:

            def __init__(self):
                self.child = {}
                self.end = False

        class PrefixTrie:

            def __init__(self):
                self.root = Node()

            def add_word(self, w):
                curr = self.root

                for c in w:
                    if c not in curr.child:
                        curr.child[c] = Node()

                    curr = curr.child[c]

                curr.end = True

        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()
        res = []

        def dfs(r, c, curr, word):

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit
            ):
                return

            l = board[r][c]

            # Questo prefisso non esiste nel Trie
            if l not in curr.child:
                return

            curr = curr.child[l]
            word += l

            visit.add((r, c))

            # Abbiamo trovato una parola
            if curr.end:
                res.append(word)
                curr.end = False

            # Continuiamo a cercare parole più lunghe
            for dr, dc in directions:
                dfs(r + dr, c + dc, curr, word)

            visit.remove((r, c))

        prefix_trie = PrefixTrie()

        for w in words:
            prefix_trie.add_word(w)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, prefix_trie.root, "")

        return res
