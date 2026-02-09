class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for values , items  in count.items():
            if items >(len(nums)//2):
                return values
        
        