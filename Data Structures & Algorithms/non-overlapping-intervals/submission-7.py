class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])

        res = 0
        interval = intervals[0]
        for start, end in intervals[1:]:
            if interval[1] > start:
                res += 1
            else:
                interval = [start, end]
        
        return res