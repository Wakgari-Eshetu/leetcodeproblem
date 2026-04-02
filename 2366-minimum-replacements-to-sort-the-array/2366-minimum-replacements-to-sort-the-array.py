class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2 , -1 ,-1):
            if nums[i] > nums[i+1]:
                k = math.ceil(nums[i] / nums[i+1])
                ans += k - 1
                nums[i] = nums[i] // k 
        
        return ans 


        