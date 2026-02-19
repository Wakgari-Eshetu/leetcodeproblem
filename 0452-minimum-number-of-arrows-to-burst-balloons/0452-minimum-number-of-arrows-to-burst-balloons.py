class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points , key= lambda x: x[1])
        result , max_dis = 0 , float(-inf)

        for start , end in points:
            if start > max_dis:
                result  += 1
                max_dis = end 
        return result 


        