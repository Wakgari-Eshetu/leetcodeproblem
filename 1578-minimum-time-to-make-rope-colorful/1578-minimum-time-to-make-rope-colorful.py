class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                if neededTime[i]<neededTime[i+1]:
                    total+=neededTime[i]
                else:
                    total+=neededTime[i+1]
        return total
        