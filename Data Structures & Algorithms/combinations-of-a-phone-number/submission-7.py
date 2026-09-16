class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        map_d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, curr):

            if i >= len(digits):
                res.append(curr)
                return
            
            for d in map_d[digits[i]]:
                backtrack(i + 1, curr + d)
            
        backtrack(0, "")
        return res



