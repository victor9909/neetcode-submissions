class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        max0, max1, max2 = [0, 0, 0]
        t1, t2, t3 = target
        for x, y, z in triplets:
            if max0 <= t1 and x <= t1 and max1 <= t2 and y <= t2 and  max2 <= t3 and z <= t3:
                max0 = max(x, max0)
                max1 = max(y, max1)
                max2 = max(z, max2)
        
        return [max0, max1, max2] == target
            