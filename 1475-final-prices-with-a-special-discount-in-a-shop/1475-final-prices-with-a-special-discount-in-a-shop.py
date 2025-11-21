class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            val = 0
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    val = prices[j]
                    
                    break
            ans.append(prices[i] - val)    
        return ans

        