class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        for x, y, w in flights:
            adj_list[x].append((w, y))
        
        min_heap = [(0, 0, src)]
        heapq.heapify(min_heap)

        while min_heap:
            len_min_heap = len(min_heap)
            w1, n_node, n = heapq.heappop(min_heap)
            
            if n_node > k + 1:
                continue

            if n == dst:
                return w1 

            for w, air_dst in adj_list[n]:
                heapq.heappush(min_heap, (w + w1, n_node + 1, air_dst))
        
        return -1
        
        