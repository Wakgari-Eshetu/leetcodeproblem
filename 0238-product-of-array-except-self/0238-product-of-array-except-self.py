class Solution(object):
    def productExceptSelf(self, nums):
        prefix_pro = [1]*len(nums)
        suffix_pro = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix_pro[i] = prefix_pro[i-1] * nums[i-1]
        for i in range(len(nums)-2 , -1 ,-1):
            suffix_pro[i] = suffix_pro[i+1] * nums[i+1]
        
        result = []
        for i in range(len(nums)):
            result.append(prefix_pro[i] * suffix_pro[i])
        
        return result 
                
        