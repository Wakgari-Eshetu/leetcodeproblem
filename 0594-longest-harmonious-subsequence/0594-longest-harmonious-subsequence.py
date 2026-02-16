class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = sorted(Counter(nums).items())
        result = 0
        for i in range(1,len(count)):
            if (count[i][0] - count[i-1][0]) == 1:
                result = max(result , count[i-1][1] + count[i][1])


        return result 
        