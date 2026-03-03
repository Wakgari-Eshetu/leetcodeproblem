class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s1 = '0'
        for i in range(n):
            invert = ''.join('1' if c == '0' else '0' for c in s1)
            s1 = s1 + '1' + invert[::-1]
        
        return s1[k-1]
        