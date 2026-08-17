class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        atl, pac = set(), set()

        def dfs(r, c, prev_height, visit):
            
            if(
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                prev_height > heights[r][c]
            ):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visit)

            return
        
        #for r in range(rows):
        #    dfs(r, 0, heights[r][0], pac)
        #    dfs(r, cols - 1, heights[r][cols - 1], atl)
        
        #for c in range(cols):
        #    dfs(0, c, heights[0][c], pac)
        #    dfs(rows - 1, c, heights[rows - 1][c], atl)

        def bfs(source, sea):
            q = deque(source)

            while q:
                len_q = len(q)
                for _ in range(len_q):
                    r, c = q.popleft()
                    sea.add((r, c))
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if(
                            row not in range(rows) or
                            col not in range(cols) or
                            (row, col) in sea or
                            heights[row][col] < heights[r][c]
                        ):
                            continue
                        q.append((row, col))
        
        pac, atl = [], []
        pac_set, atl_set = set(), set()
        for r in range(rows):
            pac.append((r, 0))
            atl.append((r, cols - 1))
            
        for c in range(cols):
            pac.append((0, c))
            atl.append((rows - 1, c))

        bfs(pac, pac_set)
        bfs(atl, atl_set)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl_set and (r, c) in pac_set:
                    res.append([r,c])
        
        return res
