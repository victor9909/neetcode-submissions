class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        class Pair():

            def __init__(self, val, dist):
                self.val = val
                self.dist = dist
            
            def __lt__(self, other):
                return self.dist > other.dist or (self.dist == other.dist and self.val > other.val)
        

        min_h = []
        for a in arr:
            pair = Pair(a, abs(a - x))
            heapq.heappush(min_h, pair)
            if len(min_h) > k:
                heapq.heappop(min_h)
        
        res = []
        while min_h:
            res.append(heapq.heappop(min_h).val)
        res.sort()
        return res