class Solution:
    def reverseBits(self, n: int) -> int:
        bit = list(format(n, '032b'))
        rev = bit[::-1]
        ans = int(''.join(rev),2)
        return ans
        