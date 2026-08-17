class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(opn, close, curr):

            if opn == close == n:
                res.append("".join(curr))
                return
            
            if opn < n:
                curr.append("(")
                backtrack(opn + 1, close, curr)
                curr.pop()

            if close < opn:
                curr.append(")")
                backtrack(opn, close + 1, curr)
                curr.pop()
            
            
        backtrack(0, 0, [])
        return res