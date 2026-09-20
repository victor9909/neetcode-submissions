class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        def is_overlap(int1, int2):
            return int1[1] >= int2[0]
        
        intervals.sort()
        if len(intervals) <= 1:
            return intervals

        res = []
        prev_int = intervals[0]
        res.append(prev_int)
        for start, end in intervals[1:]:
            if prev_int[1] >= start:
                prev_int = [min(start, prev_int[0]), max(end, prev_int[1])]
                res.pop()
            else:
                prev_int = [start, end]
            
            res.append(prev_int)
        


        return res