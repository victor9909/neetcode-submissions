class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])
        visit = set()

        def backtrack(r, c, i):

            if i >= len(word):
                return True
            
            if(
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                board[r][c] != word[i]
            ):
                return False
            
            
            visit.add((r, c))
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
            visit.remove((r, c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        return False