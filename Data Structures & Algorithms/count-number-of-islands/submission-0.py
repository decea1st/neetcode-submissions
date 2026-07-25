class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        countIslands = 0
        rowLen, colLen = len(grid), len(grid[0])

        # DFS implementation
        # directions to traverse and check neighbors
        RIGHT = (0, 1)
        LEFT = (0, -1)
        DOWN = (1, 0)
        UP = (-1, 0)
        directions = (RIGHT, LEFT, UP, DOWN)
        
        # Algorithm checks neighbor and changes 1 to 0 to mark as visited
        def dfs(row, col):
            # When to stop searching:
            # If accessing negative index, if outside range, if it finds "0"
            if (row < 0 or col < 0 or row >= rowLen or col >= colLen or
                grid[row][col] == "0"): return

            # change 1 to 0 to mark as visited
            grid[row][col] = "0"
            # check neighbors in all four directions
            for rowDir, colDir in directions:
                dfs(row + rowDir, col + colDir)

        # iterate through each element of the grid
        for row in range(rowLen):
            for col in range(colLen):
                # if "1", check neighbors through DFS search (recursive)
                if grid[row][col] == "1":
                    dfs(row, col)  # we have to implement DFS
                    countIslands += 1

        return countIslands