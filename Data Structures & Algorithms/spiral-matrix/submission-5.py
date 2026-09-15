class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, 0
        dr, dc = 0, 1

        res = []

        for _ in range(rows * cols):
            res.append(matrix[r][c])

            nr, nc = r + dr, c + dc
            
            if dr == 0 and dc == 1 and nc > right:
                dr = 1
                dc = 0
                right -= 1

            elif dr == 1 and dc == 0 and nr > bottom:
                dr = 0
                dc = -1
                bottom -= 1

            elif dr == 0 and dc == -1 and nc < left:
                dr = -1
                dc = 0
                left += 1

            elif dr == -1 and dc == 0 and nr < top +1:
                dr = 0
                dc = 1
                top += 1

            r, c = r + dr, c + dc

        return res
