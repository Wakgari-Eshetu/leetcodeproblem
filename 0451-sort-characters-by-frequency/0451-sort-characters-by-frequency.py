class Solution:
    def frequencySort(self, s: str) -> str:
        nums = Counter(s)
        nums = sorted(nums.items(),key=lambda x: -x[1])
        result = ''.join([char*f  for char,f in nums])
        return result
