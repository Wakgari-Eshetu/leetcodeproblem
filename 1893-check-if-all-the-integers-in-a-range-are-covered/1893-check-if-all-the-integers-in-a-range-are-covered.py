class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check = set()

        for start,end in ranges:
            for x in range(start,end+1):
                check.add(x)
        
        for x in range(left,right+1):
            if x not in check:
                return False 
        
        return True 

        