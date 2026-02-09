class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count =Counter(nums)

        for values , items in count.items():
            if items > (len(nums)//3):
                ans.append(values)
        return ans 