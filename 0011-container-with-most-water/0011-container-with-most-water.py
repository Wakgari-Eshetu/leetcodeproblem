class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height)-1
        max_value,cal_purpose = 0 , 0
        
        while left < right :
            width = right - left
            height_for_cal = min(height[left] , height[right])
            max_value = max(max_value, width*height_for_cal)

            if height[left] <  height[right]:
                left += 1     
            else:
                right -= 1
              
        return max_value
        