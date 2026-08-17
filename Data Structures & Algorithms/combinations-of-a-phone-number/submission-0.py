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

        def dfs(i, curr):

            if i >= len(digits):
                res.append("".join(curr))
                return
            
            num_chars = num_to_digit[digits[i]]
            for c in num_chars:
                curr.append(c)
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return res

