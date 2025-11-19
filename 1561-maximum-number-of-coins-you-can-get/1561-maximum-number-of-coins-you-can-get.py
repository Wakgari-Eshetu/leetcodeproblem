class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        piles = list(reversed(sorted(piles)))
      
        total = 0
        for i in range(1,len(piles)-n,2):
            total += piles[i]
        return total 


        