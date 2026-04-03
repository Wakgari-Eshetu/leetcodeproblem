class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        result = []
        total = rows * cols
        
        steps = 1
        r, c = rStart, cStart
        
        result.append([r, c])
        
        while len(result) < total:
            for _ in range(steps):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            for _ in range(steps):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            steps += 1
            for _ in range(steps):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            for _ in range(steps):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            steps += 1
        
        return result