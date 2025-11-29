class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        count = 0
        for c in s:
            if c == '(':
                if count > 0:
                    stack.append(c)
                count+=1
            else:
                count -=1 
                if count>0:
                    stack.append(c)
        
        return ''.join(stack)
