class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def p(n):
            value = 1
            for i in range(1,n+1):
                value*=i
            return value 
        List =[[1]]
        for i in range(1,numRows):
            l =[]
            for j in range(i+1):
                l.append(p(i)//(p(j)*p(i-j)))
            List.append(l)
        return List