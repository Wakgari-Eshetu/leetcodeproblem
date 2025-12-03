class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # using the hash map method 
        hashing = {}
        for i ,num in enumerate(nums):
            if num in hashing and i-hashing[num] <=k:
                return True 
            hashing[num] = i
        return False
