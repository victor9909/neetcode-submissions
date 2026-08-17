class Solution:
    def isValid(self, s: str) -> bool:
        
        # s = "[]" stack = []
        # [ -> stack -> ['[']
        # ] -> stack ] is what expect from [
        # { ']' : '[', ')': '(', '}': '{' }

        # s = "([{}])"
        # ( -> stack -> ['(']
        # [ -> stack -> ['(', '[']
        # { -> stack -> ['(', '[', '{']
        # } -> stack and close -> ['(', '[']
        # ] -> stack and close -> ['(']
        # ) -> stack and close -> []

        # s = "[(])"
        # [ -> stack -> ['[']
        # ( -> stack -> ['[', '(']
        # ] -> stack and close -> ['[', '(']
        # ) -> stack and close -> ['[']

        stack = []
        dict_op_cl = { ']' : '[', ')': '(', '}': '{' }
        for p in s:
            if not stack:
                stack.append(p)
            else:
                if p in dict_op_cl and dict_op_cl[p] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(p)
        
        return not stack




