class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        result = [elem for elem ,f in count.most_common(k)] 
        return result
                