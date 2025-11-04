class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            bit = list(bin(i)[2:])
            count = 0
            for j in bit:
                if j == '1':
                    count +=1        
            ans.append(count)
        return ans 