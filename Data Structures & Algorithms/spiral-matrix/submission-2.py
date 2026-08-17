class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        right_border = len(matrix[0]) - 1
        left_border = 0
        top_border = 0
        bottom_border = len(matrix) - 1

        rows = len(matrix)
        cols = len(matrix[0])
        
        res = []
        row = 0
        col = 0
        dr, dc = 0, 1

        for _ in range(rows * cols):
            res.append(matrix[row][col])

            if dc == 1 and col == right_border:        # moving right ➡️
                dr, dc = 1, 0                          # go down ⬇️
                top_border += 1
            elif dr == 1 and row == bottom_border:     # moving down ⬇️
                dr, dc = 0, -1                         # go left ⬅️
                right_border -= 1
            elif dc == -1 and col == left_border:      # moving left ⬅️
                dr, dc = -1, 0                         # go up ⬆️
                bottom_border -= 1
            elif dr == -1 and row == top_border:       # moving up ⬆️
                dr, dc = 0, 1                          # go right ➡️
                left_border += 1

            row += dr
            col += dc

        return res

                


        