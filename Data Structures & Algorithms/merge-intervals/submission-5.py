class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # ____
        #.  ____
        
        # ____
        #   _____

        # ________
        #.   ____. 

        intervals.sort(key = lambda x: x[0])
        
        def is_overlap(int1, int2):
            return int2[0] <= int1[1]
        
        
        res = [intervals[0]]
        for inte in intervals[1:]:
            if is_overlap(res[-1], inte):
                new_int = [min(res[-1][0], inte[0]), max(res[-1][1], inte[1])]
                res.pop()
                res.append(new_int)
            else:
                res.append(inte)
        return res
