class Solution:
    def sortColors(self, nums: List[int]) -> None:
        mid = left = 0
        right = len(nums)-1
        while mid<=right:
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                mid+=1
                left+=1
                
            elif nums[mid]==2:
                nums[right],nums[mid]=nums[mid],nums[right]
                
                right-=1
                
            else:
                mid+=1


        