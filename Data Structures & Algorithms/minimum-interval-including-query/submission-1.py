class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        
        # Keep the original index of each query
        queries_with_idx = sorted((q, i) for i, q in enumerate(queries))
        
        res = [-1] * len(queries)
        min_h = []
        idx = 0

        for q, original_idx in queries_with_idx:
            # Add all intervals that start before or at q
            while idx < len(intervals) and intervals[idx][0] <= q:
                start, end = intervals[idx]
                size = end - start + 1
                heapq.heappush(min_h, (size, end))
                idx += 1

            # Remove intervals that end before q
            while min_h and min_h[0][1] < q:
                heapq.heappop(min_h)

            # Smallest valid interval
            if min_h:
                res[original_idx] = min_h[0][0]

        return res