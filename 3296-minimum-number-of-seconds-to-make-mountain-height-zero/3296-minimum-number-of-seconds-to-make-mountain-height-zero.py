class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(n :int )->bool:
            ans_check = 0
            for time in workerTimes:
                max_rounds = int(sqrt(2 * n / time + 0.25) - 0.5)
                ans_check += max_rounds
            
            return ans_check >= mountainHeight
        
        left, right = 1, 10**16
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                first_true_index = mid
                right = mid - 1  
            else:
                left = mid + 1   

        return first_true_index