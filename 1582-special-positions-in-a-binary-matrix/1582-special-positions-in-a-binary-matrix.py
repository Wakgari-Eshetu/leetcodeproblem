class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows , cols = len(mat) , len(mat[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    continue 
                check =True 
                for i in range(rows):
                    if i != r and mat[i][c] == 1:
                        check = False 
                        break 
                
                for j in range(cols):
                    if j != c and mat[r][j] == 1:
                        check = False 
                        break 
                
                if check:
                    count += 1
            
        return count 
                


                     
                    