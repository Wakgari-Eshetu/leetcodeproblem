class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,tot = 0,0
        min_len = float('inf')
        for j in range(i,len(nums)):
            tot += nums[j]
            while tot >= target:
                min_len = min(min_len, j - i + 1)
                tot -= nums[i]
                i += 1
        return 0 if  min_len == float('inf') else min_len

        
            
        