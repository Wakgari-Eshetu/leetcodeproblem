class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows , cols = len(grid) , len(grid[0])
        total_sum = 0
        for row in range(rows):
            for col in range(cols):
                total_sum += grid[row][col]
        
        if total_sum % 2 == 1:
            return False
        
        target = total_sum // 2
        curr_sum = 0
        for r in range(rows - 1):
            curr_sum += sum(grid[r])
            if curr_sum == target:
                return True 
        
        curr_sum = 0
        
        for c in range(cols - 1):
            for r in range(rows):
                curr_sum += grid[r][c]
            if curr_sum == target:
                return True 

        return False 