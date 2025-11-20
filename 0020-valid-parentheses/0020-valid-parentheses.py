class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(','}':'{',']':'['}
        stack = []
        for idx in s:
            if idx not in dic:
                stack.append(idx)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != dic[idx]:
                        return False
        return not stack

        