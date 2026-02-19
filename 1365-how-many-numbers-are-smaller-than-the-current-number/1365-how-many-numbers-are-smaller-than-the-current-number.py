class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            key , count  = nums[i] ,0
           
            for j in range(len(nums)):
                if j != i and nums[j]<key:
                    count += 1
            result.append(count)
        
        return result 

        