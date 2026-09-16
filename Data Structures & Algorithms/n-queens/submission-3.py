class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        puzzle = [["."] * n for _ in range(n)]

        res = []

        def is_valid(r, c):
            
            row, col = r - 1, c
            while row >= 0:
                if puzzle[row][col] == "Q":
                    return False
                row -= 1
            
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if puzzle[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if puzzle[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            
            return True

        def backtrack(r):
            if r >= n:
                res.append(["".join(r) for r in puzzle])
                return
            
            for c in range(n):
                puzzle[r][c] = "Q"
                if is_valid(r, c):
                    backtrack(r + 1)
                puzzle[r][c] = "."
        
        backtrack(0)
        return res