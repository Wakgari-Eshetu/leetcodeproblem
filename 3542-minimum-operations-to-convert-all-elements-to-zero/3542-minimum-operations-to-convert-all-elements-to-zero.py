class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = [0]*(len(nums)+1)
        top,ans = 0,0
        for num in nums:
            while s[top]>num:
                top-=1
                ans+=1
            if s[top] != num:
                top+=1
                s[top] = num
        return ans+top
