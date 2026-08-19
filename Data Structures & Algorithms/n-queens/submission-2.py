class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        puzzle = [["."] * n for _ in range(n)]
        res = []

        def check_valid(r, c):
            # Check column
            for row in range(r):
                if puzzle[row][c] == "Q":
                    return False

    # Check upper-left diagonal
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if puzzle[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            # Check upper-right diagonal
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if puzzle[row][col] == "Q":
                    return False
                row -= 1
                col += 1

            return True

        def backtrack(row):

            if row >= n:
                res.append(["".join(r) for r in puzzle])
                return
            
            for c in range(n):
                puzzle[row][c] = "Q"
                if check_valid(row, c):
                    backtrack(row + 1)
                puzzle[row][c] = "."
        
        backtrack(0)
        return res



            