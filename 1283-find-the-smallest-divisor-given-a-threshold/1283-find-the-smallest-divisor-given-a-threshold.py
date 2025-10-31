class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def con(n:int)->bool:
            return sum((num + n -1 )//n for num in nums) <= threshold 

        left ,right = 1,max(nums)
        while left<right:
            mid = (right+left )//2
            if con(mid):
                right = mid
            else:
                left = mid+ 1
        return left
        

        