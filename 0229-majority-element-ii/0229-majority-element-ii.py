class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)//3
        return [num for num , freq in count.items() if freq > n]