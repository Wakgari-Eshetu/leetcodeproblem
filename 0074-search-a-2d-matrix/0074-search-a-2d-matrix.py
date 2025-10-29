class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        for i in range(n):
            for j in range(len(matrix[i])):
                if matrix[i][j]==target:
                    return True
        return False
        