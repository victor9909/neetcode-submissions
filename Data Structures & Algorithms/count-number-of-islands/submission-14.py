class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        par = [i for i in range((rows * cols) + 1)]
        rank = [1 for _ in range((rows * cols) + 1)]

        def find(u):
            p = par[u]
            while p != par[p]:
                p = par[p]
            return p
        
        def union(u, v):

            p1, p2 = find(u), find(v)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2

            return True
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = 0

        def index(r, c):
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    for dr, dc in directions:
                        nr, nc = dr + r, c + dc
                        if(
                            nr not in range(rows) or
                            nc not in range(cols) or
                            grid[nr][nc] == "0"
                        ):
                            continue
                        
                        if union(index(r, c), index(nr, nc)):
                            res -= 1
        
        return res


        
