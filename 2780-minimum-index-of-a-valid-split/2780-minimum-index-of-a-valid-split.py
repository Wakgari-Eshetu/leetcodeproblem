class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant_x , x_count = Counter(nums).most_common(1)[0]
        
        left_count = 0

        for index , value in enumerate(nums,1):
            if value == dominant_x:
                left_count += 1
            
            dominant_in_left = left_count*2  > index
            dominant_in_right = (x_count - left_count) * 2 > len(nums) - index

            if dominant_in_left and  dominant_in_right:
                return index - 1
        
        return -1