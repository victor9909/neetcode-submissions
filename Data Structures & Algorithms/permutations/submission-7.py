class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        def backtrack(idx, nums):

            if idx == len(nums):
                return [[]]
            
            res_perm = []
            perms = backtrack(idx + 1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    p_cop = p[::]
                    p_cop.insert(j, nums[idx])
                    res_perm.append(p_cop)
            return res_perm
        
        return backtrack(0, nums)

