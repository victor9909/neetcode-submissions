class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        row = None

        while top <= bot:
            row = (top + bot) // 2

            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False