class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        top = 1
        ans = 0
        i = 0
        while top <= n:
            if i < len(nums) and nums[i] <= top:
                top += nums[i]
                i += 1
            else:
                top += top
                ans += 1
        return ans 

