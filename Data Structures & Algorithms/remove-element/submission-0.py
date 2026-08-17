class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        res_arr = []
        for n in nums:
            if n != val:
                res_arr.append(n)
        
        nums[::] = res_arr[::]

        return len(res_arr)