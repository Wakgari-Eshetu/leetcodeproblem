class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        ans = 0 
        left , middle = 0 , 0
        for right in range(len(nums)):
            count[nums[right]] += 1

            while len(count) > k:
                count[nums[middle]] -= 1
                if count[nums[middle]] == 0:
                    count.pop(nums[middle])
                middle += 1
                left = middle 
            
            while count[nums[middle]] > 1:
                count[nums[middle]] -= 1 
                middle += 1
            
            if len(count) == k:
                ans  += middle - left + 1

        return ans  