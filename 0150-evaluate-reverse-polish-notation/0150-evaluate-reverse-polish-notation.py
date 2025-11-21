class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val  in tokens:
            if val in '+-*/':
                b,a = stack.pop(),stack.pop()
                if val == '+':
                    stack.append(a+b)
                elif val == '-':
                    stack.append(a-b)
                elif val == '*':
                    stack.append(a*b)
                if val == '/':
                    div = a/b
                    if div<0:
                        stack.append(ceil(div))
                    else:
                        stack.append(floor(div))
            else:
                stack.append(int(val)) 

        return stack[0]
        