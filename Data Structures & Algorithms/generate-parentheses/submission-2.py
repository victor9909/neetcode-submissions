class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #               .
        #           (       .
        #       ((    ()
        #   (((    ((   
        #

        res = []
        def backtrack(opn, cls, curr):
            
            if opn > n or cls > n:
                return

            if opn == cls == n:
                res.append("".join(curr))
                return
            
            if opn < n:
                curr.append("(")
                backtrack(opn + 1, cls, curr)
                curr.pop()

            if opn > cls:
                curr.append(")")
                backtrack(opn, cls + 1, curr)
                curr.pop()
                
        
        backtrack(0, 0, [])
        return res
        
