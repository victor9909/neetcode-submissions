class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        arr = [[] for _ in range(max(count.values()) + 1)]
        for key in count:
            arr[count[key]].append(key)
        
        res = []
        for f in arr[::-1]:
            for e in f:
                res.append(e)
                if len(res) == k:
                    return res
