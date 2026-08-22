# Last updated: 8/22/2026, 9:51:45 AM
1class Solution:
2    def minPathSum(self, grid):
3
4        m = len(grid)
5        n = len(grid[0])
6
7        for i in range(m):
8            for j in range(n):
9
10                if i == 0 and j == 0:
11                    continue
12
13                elif i == 0:
14                    grid[i][j] += grid[i][j - 1]
15
16                elif j == 0:
17                    grid[i][j] += grid[i - 1][j]
18
19                else:
20                    grid[i][j] += min(
21                        grid[i - 1][j],
22                        grid[i][j - 1]
23                    )
24
25        return grid[m - 1][n - 1]