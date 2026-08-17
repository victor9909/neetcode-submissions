class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        

        count = Counter(nums)
        res = []

        def backtrack(perm):

            if len(perm) == len(nums):
                res.append(perm[::])
                return
            
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    perm.append(c)

                    backtrack(perm)

                    count[c] += 1
                    perm.pop()
        
        backtrack([])
        return res