class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(grid, row, col, visited):
            position = (row, col)
            if not(0<=row<rows) or not(0<=col<cols):
                return False
            if position in visited:
                return False
            visited.add(position)
            if grid[row][col] == 0:
                grid[row][col] = 'Y'                    
                dfs(grid, row - 1, col, visited)
                dfs(grid, row + 1, col, visited)
                dfs(grid, row, col - 1, visited)
                dfs(grid, row, col + 1, visited)
            # return True

        visited = set()
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    dfs(grid, row, col, visited) 
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    counter += 1
        return counter