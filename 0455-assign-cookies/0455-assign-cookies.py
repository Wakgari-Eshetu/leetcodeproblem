class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
    
        g.sort()
        s.sort()

        ch ,ck = 0,0
        while ch<len(g) and ck<len(s):
            if g[ch] <= s[ck]:
                ch+=1
            ck +=1
        return ch
         