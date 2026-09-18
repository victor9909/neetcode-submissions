class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # [[0,0],[2,2],[3,3],[2,4],[4,2]]
        nodes = [i for i in range(len(points))]
        adj_list = {i:[] for i in range(len(points))}
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if p1 == p2:
                    continue
                adj_list[i].append((abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), j))
        
        res = 0
        min_h = [[0, 0]]
        visit = set()
        while min_h:
            cost, i = heapq.heappop(min_h)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nei_cost, nei in adj_list[i]:
                heapq.heappush(min_h, [nei_cost, nei])
        return res