class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands