class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        #using maths for solving the  question 
        cycle = 2*(n-1)
        ti = time % cycle 
        if ti < n:
            return ti+1
        else:
            return n-(ti-(n-1)) 
        