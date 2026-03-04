class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        check_sum  = 0
        for i in range(k):
            check_sum += nums[i] 
        
        result = check_sum 
        for i in range(k , len(nums)):
            check_sum -= nums[i-k]
            check_sum += nums[i]
            result = max(result , check_sum )
        
        return result / k




        