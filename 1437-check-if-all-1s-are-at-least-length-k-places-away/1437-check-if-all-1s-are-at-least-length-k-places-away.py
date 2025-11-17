class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == 1:
                for j in range(i+1,len(nums)):
                    if nums[j] == 1:
                        if j-i-1 < k:
                            return False
                        break
        return True




        