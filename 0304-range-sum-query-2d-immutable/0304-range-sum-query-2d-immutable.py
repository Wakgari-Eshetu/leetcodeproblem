class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self._sum = [[0 for _ in range(cols + 1)] for _ in range(rows)]
        for i in range(rows):
            cur_sum = 0
            for j in range(cols):
                cur_sum += matrix[i][j]
                self._sum[i][j+1] = cur_sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum([row[col2+1] - row[col1] for row in self._sum[row1:row2+1]])
        
        
