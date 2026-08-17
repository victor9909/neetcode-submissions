class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bot = 0, len(matrix) - 1
        row = (top + bot) // 2

        while top <= bot:
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
            row = (top + bot) // 2
        
        cols = len(matrix[0])
        l = 0
        r = cols - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False