class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        def check_overlap(int1, int2):
            return int1[1] >= int2[0]

        res = [intervals[0]]
        for interval in intervals[1:]:
            if check_overlap(res[-1], interval):
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        
        return res