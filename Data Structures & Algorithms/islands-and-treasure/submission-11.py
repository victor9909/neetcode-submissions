class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 1

        while q:
            len_q = len(q)
            for _ in range(len_q):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if(
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] != -1 and
                        (nr, nc) not in visit
                    ):
                        grid[nr][nc] = dist
                        visit.add((nr, nc))
                        q.append((nr, nc))
            dist += 1
        









