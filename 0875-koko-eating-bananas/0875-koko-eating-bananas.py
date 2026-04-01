class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        def check_fun(mid):
            hour = 0
            for pile in piles:
                hour += (pile + mid - 1) // mid 
            return hour <= h
            

        left , right = 1 , max(piles)
        while left <= right:
            mid = left + (right - left) // 2 
            if check_fun(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left 