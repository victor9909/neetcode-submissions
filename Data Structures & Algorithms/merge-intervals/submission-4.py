class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        res = []
        new_interval = intervals[0]

        for i in range(1, len(intervals)):

            curr = intervals[i]

            # ❌ Nessuna sovrapposizione
            if new_interval[1] < curr[0]:
                res.append(new_interval)
                new_interval = curr

            # ✅ Sovrapposizione → fondiamo
            else:
                new_interval[1] = max(new_interval[1], curr[1])

        # aggiungiamo l'ultimo intervallo
        res.append(new_interval)

        return res
            