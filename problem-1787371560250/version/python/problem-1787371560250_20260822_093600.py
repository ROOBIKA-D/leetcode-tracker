# Last updated: 8/22/2026, 9:36:00 AM
1class Solution:
2    def minDistance(self, word1, word2):
3
4        m = len(word1)
5        n = len(word2)
6
7        dp = [[0] * (n + 1) for _ in range(m + 1)]
8
9        # Convert empty word1 to word2
10        for j in range(n + 1):
11            dp[0][j] = j
12
13        # Convert word1 to empty word2
14        for i in range(m + 1):
15            dp[i][0] = i
16
17        for i in range(1, m + 1):
18            for j in range(1, n + 1):
19
20                if word1[i - 1] == word2[j - 1]:
21                    dp[i][j] = dp[i - 1][j - 1]
22
23                else:
24                    insert = dp[i][j - 1]
25                    delete = dp[i - 1][j]
26                    replace = dp[i - 1][j - 1]
27
28                    dp[i][j] = 1 + min(insert, delete, replace)
29
30        return dp[m][n]