class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        time = 0
        visit = set()
        q = [(0, k)]
        heapq.heapify(q)

        while q:
            len_q = len(q)
            for _ in range(len_q):
                wu, u = heapq.heappop(q)
                if u in visit:
                    continue
                time = wu
                visit.add(u)

                if len(visit) == n:
                    return time

                for v, w in adj_list[u]:
                    if v in visit:
                        continue
                    heapq.heappush(q, (w + wu, v))
        return -1
        
