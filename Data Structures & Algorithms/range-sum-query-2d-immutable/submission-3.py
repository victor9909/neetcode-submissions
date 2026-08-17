class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.prefix = defaultdict(int)
        rows, cols = len(matrix), len(matrix[0])
        self.rows, self.cols = rows, cols
        for r in range(rows):
            curr = 0
            for c in range(cols):
                curr += matrix[r][c]
                self.prefix[(r, c)] = curr

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        res = 0
        for r in range(row1, row2 + 1):
            left = self.prefix[(r, min(col1, col2) - 1)] if min(col1, col2) > 0 else 0
            right = self.prefix[(r, max(col1, col2))]
            res += right - left
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)