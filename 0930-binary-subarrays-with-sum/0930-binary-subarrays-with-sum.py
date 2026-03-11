class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 
        current_sum = 0
        ans = 0

        for num in nums:
            current_sum += num
            ans += prefix_count[current_sum - goal]
            prefix_count[current_sum] += 1

        return ans