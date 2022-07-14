class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col, visited):
            if not(0 <= row < rows) or not(0 <= col < colms):
                return 0
            position = (row, col)
            if position in visited:
                return 0
            if grid[row][col] == 0:
                return 0

            visited.add(position)

            size = 1
            size += dfs(grid, row - 1, col, visited)
            size += dfs(grid, row + 1, col, visited)
            size += dfs(grid, row, col - 1, visited)
            size += dfs(grid, row, col + 1, visited)

            return size

        rows = len(grid)
        colms = len(grid[0])
        max_area = 0
        visited = set()
        for row in range(rows):
            for col in range(colms):
                new_max = dfs(grid, row, col, visited)
                if new_max > max_area:
                    max_area = new_max
        return max_area
