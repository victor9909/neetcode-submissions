class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        curr = []

        def backtrack(opn, cls):

            if opn == cls == n:
                res.append("".join(curr[::]))
                return
            
            if opn < n:
                curr.append("(")
                backtrack(opn + 1, cls)
                curr.pop()
            
            if cls < opn:
                curr.append(")")
                backtrack(opn, cls + 1)
                curr.pop()
        
        backtrack(0, 0)
        return res
