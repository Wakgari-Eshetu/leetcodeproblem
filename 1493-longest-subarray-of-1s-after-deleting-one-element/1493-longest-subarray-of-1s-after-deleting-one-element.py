class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left , right , ans = 0, 0, 0
        count = Counter()
        while right < len(nums):
            count[nums[right]] += 1
            while count[0] > 1:
                if nums[left] == 0:
                    count[0] -= 1
                left += 1
            ans = max(ans , right-left)
            right += 1
        
        return ans 




        