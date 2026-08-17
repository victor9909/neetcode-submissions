class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bot = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        row = None

        while top <= bot:

            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False

