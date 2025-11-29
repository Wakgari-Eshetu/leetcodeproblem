class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c.lower() == stack[-1].lower() and c.isupper()!=stack[-1].isupper():
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack) 

        