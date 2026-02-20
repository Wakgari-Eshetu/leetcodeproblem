class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row , col = len(matrix) , len(matrix[0])
        row_idx = set()
        col_idx = set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    row_idx.add(r)
                    col_idx.add(c)
                    
        for r in row_idx:
            for c in range(col):
                matrix[r][c] = 0
        for c in col_idx:
            for r in range(row):
                matrix[r][c] = 0         
        return matrix 
                    
        