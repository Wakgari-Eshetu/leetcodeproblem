class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse= True)

        for h in range(len(citations) , -1 , -1):
            if citations[h-1] >= h:
                return h
        return 0
        