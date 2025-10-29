class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]==target:
                return i
        else:
            nums.append(target)
            nums=sorted(nums)
            m=len(nums)
            for j in range(m):
                if nums[j]==target:
                    return j
                    
        