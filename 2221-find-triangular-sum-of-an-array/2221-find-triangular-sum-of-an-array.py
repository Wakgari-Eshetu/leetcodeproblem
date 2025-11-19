class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        while len(nums)>1:
            n = len(nums)
            newNums = [0]*(n-1)
            for i in range(n-1):
                newNums[i] = (nums[i]+nums[i+1])%10
            nums = newNums
        return nums[0]