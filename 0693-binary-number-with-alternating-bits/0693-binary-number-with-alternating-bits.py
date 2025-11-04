class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        v = list(bin(n)[2:])
        for i in range(len(v)-1):
            if v[i]==v[i+1]:
                return False
        return True
        