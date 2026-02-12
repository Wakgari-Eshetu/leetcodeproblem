class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = nums[i-1]*2
                nums[i] = 0
        result = []
        for i in nums:
            if i != 0:
                result.append(i)
        zeros = len(nums)-len(result)
        result.extend([0]*zeros)
        return result 

        