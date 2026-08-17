class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0
        curr = 0
        res = 0

        for r in range(len(arr)):
            
            curr += arr[r]
            if r - l + 1 < k:
                continue

            curr_threshold = curr / k
            if curr_threshold >= threshold:
                res += 1
            curr -= arr[l]
            l += 1

        return res


            
            
            
