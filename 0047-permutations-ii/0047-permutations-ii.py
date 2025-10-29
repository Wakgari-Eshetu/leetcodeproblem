class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums = sorted(nums)
        result = []
        check = []
        used = [False]*n
        def check_out():
            if len(check)==n:
                result.append(check[:])
            for i in range(n):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                check.append(nums[i])
                check_out()
                check.pop()
                used[i]=False
        check_out()
        return result
            