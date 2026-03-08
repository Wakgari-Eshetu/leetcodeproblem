class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        count = {0:1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in count:
                result += count[prefix_sum - k]
            count[prefix_sum] = count.get(prefix_sum , 0) + 1
        
        return result 
        
        