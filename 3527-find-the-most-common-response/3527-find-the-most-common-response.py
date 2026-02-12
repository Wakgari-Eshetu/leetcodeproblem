class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        result = []
        result1 = []
        for i in responses:
            for j in i:
                if j not in result1:
                    result1.append(j)
            result.extend(result1)   
            result1 = []

        count = Counter(result)
        max_count = max (count.values())
        candidate = [k for k,v in count.items() if v == max_count]
        return min(candidate)
        