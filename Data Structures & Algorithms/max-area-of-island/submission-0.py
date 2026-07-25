class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_area= 0
        row_num, col_num = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

        def dfs(row, col):
            if (row < 0 or row >= row_num or col < 0 or
                col >= col_num or grid[row][col] == 0):
                return 0

            grid[row][col] = 0

            return 1 + sum(dfs(row + dr, col + dc) for dr, dc in directions)

        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    if area > max_area:
                        max_area = area

        return max_area