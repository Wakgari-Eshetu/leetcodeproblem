class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows , cols = len(grid) , len(grid[0])
        prefix_sum = [[0]*(cols + 1)  for _ in range(rows + 1)]
        
        ans = 0
        for row in range(rows):
            for col in range(cols):
                prefix_sum[row][col] = prefix_sum[row - 1][col] + prefix_sum[row][col - 1] -prefix_sum[row - 1][col - 1] + grid[row][col]

                if prefix_sum[row][col] <= k:
                    ans += 1
        return ans 
        