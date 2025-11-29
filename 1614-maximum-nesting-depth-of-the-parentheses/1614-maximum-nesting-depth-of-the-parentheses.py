class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        depth = 0
        for c in s:
            if c =="(":
                count+=1
                depth = max(depth,count)
            else:
                if c == ')':
                    count -= 1
        return depth 
        