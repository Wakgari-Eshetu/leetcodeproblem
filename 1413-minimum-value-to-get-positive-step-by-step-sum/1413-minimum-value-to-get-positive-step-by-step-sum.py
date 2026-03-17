class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        
        return  1 if 1 - min(nums) <= 0 else 1 - min(nums)
        