class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                ans.append(nums[i])
                ans.append(nums[i]+1)
                break
        return ans 

        