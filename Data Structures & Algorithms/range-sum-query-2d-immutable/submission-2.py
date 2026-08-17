class NumMatrix:

    # 1 2 3
    # 1 2 3
    # 1 2 3

    def __init__(self, matrix: List[List[int]]):
        self.prefix_m = defaultdict(list)
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            tot = 0
            for c in range(cols):
                tot += matrix[r][c]
                self.prefix_m[r].append(tot)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        res = 0
        for r in range(row1, row2 + 1):
            right = self.prefix_m[r][max(col1, col2)]
            left = self.prefix_m[r][min(col1, col2) - 1] if min(col1, col2) > 0 else 0
            res +=  right - left
            
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)