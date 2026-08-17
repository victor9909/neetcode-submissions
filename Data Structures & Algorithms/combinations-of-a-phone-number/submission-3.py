class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        if not digits:
            return []

        def backtrack(curr, i):

            if i >= len(digits):
                res.append("".join(curr[::]))
                return
            
            for c in digits_map[digits[i]]:
                curr.append(c)
                backtrack(curr, i + 1)
                curr.pop()
        
        backtrack([], 0)
        return res


