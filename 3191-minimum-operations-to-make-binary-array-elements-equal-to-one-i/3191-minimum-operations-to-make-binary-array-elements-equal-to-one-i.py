class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i + 2 >= len(nums):
                    return -1 
                for j in range(3):
                    nums[i+j]  = 0 if nums[i+j] == 1 else 1 
                
                count += 1
        return count 
                
        
            

        