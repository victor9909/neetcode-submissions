class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        idx = m + n - 1
        i = m - 1
        j = n - 1
        
        while i >= 0 or j >= 0:
            val1 = nums1[i] if i >= 0 else None
            val2 = nums2[j] if j >= 0 else None

            if val1 != None and val2 != None:
                if val1 > val2:
                    nums1[idx] = val1
                    i -= 1
                else:
                    nums1[idx] = val2
                    j -= 1
            else:
                if val1 == None and val2 != None:
                    nums1[idx] = val2
                    j -= 1
                if val2 == None and val1 != None:
                    nums1[idx] = val1
                    i -= 1
            idx -= 1
        


        