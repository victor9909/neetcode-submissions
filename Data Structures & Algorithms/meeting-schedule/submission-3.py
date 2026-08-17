"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        def is_overlap(int1, int2):
            return int2.start < int1.end
        
        intervals.sort(key = lambda x: x.start)
        prev = intervals[0]
        for inte in intervals[1:]:
            if is_overlap(prev, inte):
                return False
            else:
                prev = inte
        
        return True