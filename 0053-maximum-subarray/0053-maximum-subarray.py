class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            prefix_sum = max(nums[i] , prefix_sum + nums[i])
            result = max(prefix_sum , result)
        
        return result 
        
        