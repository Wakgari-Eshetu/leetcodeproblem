class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        for char in nums:
            if char == target:
                return True 
        return False

                

        