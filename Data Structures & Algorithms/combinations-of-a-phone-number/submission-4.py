class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        map_digit = {
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
        curr = []

        def backtrack(i):

            if i >= len(digits):
                if curr:
                    res.append("".join(curr[::]))
                return
            
            for d in map_digit[digits[i]]:
                curr.append(d)
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return res
