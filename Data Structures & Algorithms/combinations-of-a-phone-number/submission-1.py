class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        num_to_digit = {
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

        def backtrack(curr, idx):
            
            if idx >= len(digits):
                res.append("".join(curr[::]))
                return
            
            for c in num_to_digit[digits[idx]]:
                curr.append(c)
                backtrack(curr, idx + 1)
                curr.pop()
            
        backtrack([], 0)
        return res

