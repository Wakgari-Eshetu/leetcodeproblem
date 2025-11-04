class Solution:
    def reverseBits(self, n: int) -> int:
        bit = list(format(n, '032b'))
        left,right  = 0 ,len(bit)-1
        while left<right:
            bit[left],bit[right]=bit[right],bit[left]
            left+=1
            right -=1
        ans = int(''.join(bit),2)
        return ans
        