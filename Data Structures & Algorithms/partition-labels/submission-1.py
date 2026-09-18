class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_idx = {}
        for i, c in enumerate(s):
            last_idx[c] = i
        
        end, size, res = 0, 0, []

        for i, c in enumerate(s):
            end = max(end, last_idx[c])
            size += 1

            if end == i:
                res.append(size)
                size = 0
        return res

