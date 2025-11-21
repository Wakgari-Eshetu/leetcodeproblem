class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s =[]
        for i in s:
            if i != "#":
                stack_s.append(i)
            else:
                stack_s.pop()
                    
        stack_t =[]
        for i in t:
            if i != "#":
                stack_t.append(i)
            else:
                stack_t.pop()
        return stack_s==stack_t