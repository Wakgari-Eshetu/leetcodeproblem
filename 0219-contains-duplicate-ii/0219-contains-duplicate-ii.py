class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0 
        while i < len(nums) -1:
            j = len(nums) - 1
            while i<j:
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
                j-=1
            i+=1
        return False