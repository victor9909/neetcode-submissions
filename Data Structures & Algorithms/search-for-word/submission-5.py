class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(r, c, visit, idx):
            if idx == len(word):
                return True
            
            if(
                c not in range(cols) or
                r not in range(rows) or
                (r, c) in visit or
                board[r][c].lower() != word[idx].lower()
            ):
                return False
            
            visit.add((r, c))
            res = backtrack(r, c + 1, visit, idx + 1) or backtrack( r + 1, c, visit, idx + 1) or backtrack( r,c - 1, visit, idx + 1) or backtrack( r - 1,c, visit, idx + 1) 
            visit.remove((r, c))
            
            return res

        for r in range(rows):
            for c in range(cols):
                print(r, c)
                if backtrack(r, c, set(), 0):
                    return True
        
        return False




        
