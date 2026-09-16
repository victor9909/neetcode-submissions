class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def backtrack(r, c, i):
            
            if i >= len(word):
                return True

            if(
                r not in range(rows) or
                c not in range(cols) or
                board[r][c] != word[i]
            ):
                return False

            
            board[r][c] = "#"
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
            board[r][c] = word[i]

            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        print(r, c)
                        return True
        return False


