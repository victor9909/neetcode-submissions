class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((w, v))
        
        min_heap = [(0, k)]
        heapq.heapify(min_heap)
        visit = set()
        t = 0

        while min_heap:
            w, v = heapq.heappop(min_heap)
            if v in visit:
                continue
            visit.add(v)
            t = max(t, w)

            for nei_w, nei_v in edges[v]:
                if nei_v not in visit:
                    heapq.heappush(min_heap, (nei_w + w, nei_v))
        
        return t if len(visit) == n else -1
        