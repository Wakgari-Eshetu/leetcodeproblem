class Solution:
    def hammingWeight(self, n: int) -> int:
        lists = list(bin(n)[2:])
        count = 0
        for i in lists:
            if i == "1":
                count +=1 
            
        return count
        