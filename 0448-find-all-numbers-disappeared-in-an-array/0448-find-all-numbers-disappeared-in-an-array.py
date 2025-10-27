class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = set(nums)
        ans = []
        for i in range(1,n+1):
            if i not in check:
                ans.append(i)
        return ans
        