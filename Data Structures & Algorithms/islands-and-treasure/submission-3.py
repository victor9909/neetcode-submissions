class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        def addRoom(r, c):
            if(
                r < 0 or c < 0 or r == ROWS or c == COLS or
                grid[r][c] == -1 or (r, c) in visit
            ):
                return
            
            visit.add((r, c))
            q.append((r, c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)
            dist += 1
        

