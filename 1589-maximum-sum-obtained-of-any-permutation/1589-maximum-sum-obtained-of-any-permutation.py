class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = pow(10 , 9) + 7
        count = [0]*len(nums)
        for start , end  in requests:
            count[start] += 1
            if end + 1 < len(nums):
                count[end+1] -= 1
        
        for i in range( 1, len(nums)):
            count[i] += count[i-1]
        
        nums.sort()
        count.sort()

        return sum( a*b  for a ,b in  zip(nums , count)) % mod
        

