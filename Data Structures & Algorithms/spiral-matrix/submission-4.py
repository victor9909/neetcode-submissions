class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, 0
        dr, dc = 0, 1

        res = []

        for _ in range(rows * cols):
            res.append(matrix[r][c])

            nr, nc = r + dr, c + dc

            if dr == 0 and dc == 1 and nc >= right:
                dr, dc = 1, 0
                top += 1

            elif dr == 1 and dc == 0 and nr >= bottom:
                dr, dc = 0, -1
                right -= 1

            elif dr == 0 and dc == -1 and nc < left:
                dr, dc = -1, 0
                bottom -= 1

            elif dr == -1 and dc == 0 and nr < top:
                dr, dc = 0, 1
                left += 1

            r, c = r + dr, c + dc

        return res
