class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result ,finding = [],[]
        def check_out():
            if len(finding)==n:
                result.append(finding[:])
                return result
            for char in nums:
                if char not in finding:
                    finding.append(char)
                    check_out()
                    finding.pop()
        check_out()
        return result
        