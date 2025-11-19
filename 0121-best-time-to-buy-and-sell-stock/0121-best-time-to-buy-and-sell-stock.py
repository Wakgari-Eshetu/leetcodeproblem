class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max =0 
        min =float('inf')
        for price in prices:
            if price < min:
                min = price 
            profit = price - min
            if profit > max :
                max = profit
        return max 