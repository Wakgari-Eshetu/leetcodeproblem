class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        check_sum = 0
        dicts = {0:-1}
        for i , num in enumerate(nums):
            check_sum += num
            if k != 0:
                check_sum %= k 
            if check_sum in dicts:
                if i - dicts[check_sum] > 1:
                    return True 
            else:
                dicts[check_sum ] = i
        return False 
            

        