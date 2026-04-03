class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        count_even = (n + 1) // 2
        count_odd = n // 2

        
        
        return pow(5 , count_even , mod ) * pow(4 , count_odd , mod) % mod