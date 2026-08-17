class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        
        res = []

        idx0, idx1 = 0, 0
        while idx0 < len1 and idx1 < len2:
            if nums1[idx0] < nums2[idx1]:
                res.append(nums1[idx0])
                idx0 += 1
            else:
                res.append(nums2[idx1])
                idx1 += 1
        
        for i in range(idx0, len1):
            res.append(nums1[i])
        
        for i in range(idx1, len2):
            res.append(nums2[i])
        print(res)
        totalLen = len(res)
        if totalLen % 2 == 0:
            return (res[totalLen // 2 - 1] + res[totalLen // 2]) / 2.0
        else:
            return res[totalLen // 2]