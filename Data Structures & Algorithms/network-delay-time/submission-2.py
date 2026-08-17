class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for src, dst, w in times:
            adj[src].append((w, dst))
        
        min_heap = [(0, k)]
        heapq.heapify(min_heap)
        visit = set()
        time = 0

        while min_heap:
            len_min_heap = len(min_heap)
            for _ in range(len_min_heap):
                w1, n1 = heapq.heappop(min_heap)
                visit.add(n1)
                time = w1
                
                if len(visit) == n:
                    return time

                for w, dst in adj[n1]:
                    if dst not in visit:
                        heapq.heappush(min_heap, (w1 + w, dst))
        
        return time if len(visit) == n else -1