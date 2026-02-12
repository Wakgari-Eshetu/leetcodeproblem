class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        
        return [value for value,index in count.most_common(k)]
        


        
        