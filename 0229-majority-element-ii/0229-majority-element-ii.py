class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return  [x  for x in count if count[x] > len(nums)/3]
        