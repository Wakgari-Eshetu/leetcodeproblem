class Solution:
    def arrangeCoins(self, n: int) -> int:
        count =0 
        tot = 0
        for i in range(n+1):
            tot+=i
            if tot > n:
                return i-1
            if tot == n:
                return i

        