class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i, j) -> bool:
            if i >= len(s):
                return True
          
            current_value = 0
            k = len(s) - 1 if j < 0 else len(s)
          
            
            for t in range(i, k):
                current_value = current_value * 10 + int(s[t])
                if (j < 0 or j - current_value == 1):
                    if backtrack(t + 1, current_value):
                        return True
          
            return False
        return backtrack(0, -1)
        