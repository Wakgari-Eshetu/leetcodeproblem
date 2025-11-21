class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i not in ["D","C","+"]:
                stack.append(int(i))
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                val = 2*stack[-1]
                stack.append(val)
            elif i == '+':
                val = stack[-1] + stack[-2]
                stack.append(val)
        return sum(stack)
    


        