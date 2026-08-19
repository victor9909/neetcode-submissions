class Solution:
    def totalNQueens(self, n: int) -> int:
        
        puzzle = [["."] * n for _ in range(n)]
        res = 0

        def check_valid(r, c):

            for i in range(r):
                if puzzle[i][c] == "Q":
                    return False
            
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if puzzle[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if puzzle[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            
            return True
        

        def backtrack(row):
            nonlocal res
            if row >= n:
                res += 1
                return
            
            for col in range(n):
                puzzle[row][col] = "Q"
                if check_valid(row, col):
                    backtrack(row + 1)
                puzzle[row][col] = "."
            
        
        backtrack(0)
        return res



