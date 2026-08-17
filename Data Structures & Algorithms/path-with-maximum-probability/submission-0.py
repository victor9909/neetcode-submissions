class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        

        adj = defaultdict(list)
        for i, pnt in enumerate(edges):
            adj[pnt[0]].append((-1 * succProb[i], pnt[1]))
            adj[pnt[1]].append((-1 * succProb[i], pnt[0]))
        
        min_heap = [(-1, start_node)]
        heapq.heapify(min_heap)
        visit = set()

        prob = 0
        while min_heap:
            len_min_heap = len(min_heap)
            for _ in range(len_min_heap):
                w1, n = heapq.heappop(min_heap)
                
                if n in visit:
                    continue
                
                visit.add(n)
                prob = w1
                if n == end_node:
                    return prob * -1
                
                for w, dst in adj[n]:
                    if dst not in visit:
                        heapq.heappush(min_heap, (-1 * w1 * w, dst))
        
        return 0



