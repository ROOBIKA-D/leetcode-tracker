# Last updated: 8/22/2026, 9:50:42 AM
1class Solution:
2    def uniquePaths(self, m, n):
3
4        dp = [[1] * n for _ in range(m)]
5
6        for i in range(1, m):
7            for j in range(1, n):
8                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
9
10        return dp[m - 1][n - 1]