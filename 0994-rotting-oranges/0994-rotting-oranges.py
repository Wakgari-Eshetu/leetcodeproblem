class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0 :
            return 0
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            size = len(queue)
            rotten = False 
            for _ in range(size):
                r , c = queue.popleft()
                for dir_row , dir_col in directions:
                    new_row , new_col = r + dir_row , c + dir_col
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row ][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row  , new_col)) 
                        fresh -= 1
                        rotten = True 
            if rotten:
                minutes += 1

        return minutes if fresh == 0 else -1 



        