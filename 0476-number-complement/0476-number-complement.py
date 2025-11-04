class Solution:
    def findComplement(self, num: int) -> int:
        v = list(bin(num)[2:])
        ans = []
        for i in v:
            if i == '1':
                ans.append('0')
            else:
                ans.append('1')
        return int(''.join(ans),2)
        