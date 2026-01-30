class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for key, value in counter.items():
            if value  > (len(nums)//2):
                return key
        