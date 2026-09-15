class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zero_first_column = False
        zero_first_row = False
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            if matrix[r][0] == 0:
                zero_first_column = True
        
        for c in range(cols):
            if matrix[0][c] == 0:
                zero_first_row = True
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if zero_first_row:
            for c in range(cols):
                matrix[0][c] = 0
        
        if zero_first_column:
            for r in range(rows):
                matrix[r][0] = 0





