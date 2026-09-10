class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        max_f = max(freq.values())
        arr = [[] for _ in range(max_f + 1)]

        for key in freq:
            arr[freq[key]].append(key)
        
        print(arr)
        res = []
        for l in arr[::-1]:
            for n in l:
                res.append(n)
                if len(res) == k:
                    return res

