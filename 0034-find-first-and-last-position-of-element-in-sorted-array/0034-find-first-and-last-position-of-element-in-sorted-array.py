class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left,right=-1,-1
        i,j=0,n-1
        while i<n and j>-1:
            if nums[i]==target and left==-1:
                left=i
            else:
                i+=1
            if nums[j]==target and right==-1:
                right=j
            else:
                j-=1
            if left!=-1 and right!=-1:
                break

        return [left,right]
                

        
        
        