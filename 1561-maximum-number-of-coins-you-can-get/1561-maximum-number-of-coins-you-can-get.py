class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0
        piles = sorted(piles , reverse= True)
        j , k =  1 , len(piles)-1
        while j < k :
            result += piles[j]
            j += 2
            k -= 1
        return result 

        


        