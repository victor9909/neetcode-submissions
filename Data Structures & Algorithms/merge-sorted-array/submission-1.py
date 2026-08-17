class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j = m - 1, n - 1
        tmp = 0
        for idx in range(m + n - 1, -1, -1):
            if i < 0 or j < 0:
                tmp = idx
                break
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
        
        while j >= 0:
            nums1[tmp] = nums2[j]
            j -= 1
            tmp -= 1

         
        
        
        


            
