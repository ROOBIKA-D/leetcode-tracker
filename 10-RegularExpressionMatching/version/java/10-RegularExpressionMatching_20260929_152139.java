// Last updated: 9/29/2026, 3:21:39 PM
1class Solution {
2    public boolean isMatch(String s, String p) {
3        int m = s.length();
4        int n = p.length();
5
6        boolean[][] dp = new boolean[m + 1][n + 1];
7
8        dp[0][0] = true;
9
10        for (int j = 2; j <= n; j++) {
11            if (p.charAt(j - 1) == '*') {
12                dp[0][j] = dp[0][j - 2];
13            }
14        }
15
16        for (int i = 1; i <= m; i++) {
17            for (int j = 1; j <= n; j++) {
18
19                char pc = p.charAt(j - 1);
20                char sc = s.charAt(i - 1);
21
22                if (pc == '.' || pc == sc) {
23                    dp[i][j] = dp[i - 1][j - 1];
24                }
25
26                else if (pc == '*') {
27                    // '*' matches zero occurrences
28                    dp[i][j] = dp[i][j - 2];
29
30                    // '*' matches one or more occurrences
31                    if (p.charAt(j - 2) == '.' ||
32                        p.charAt(j - 2) == sc) {
33                        dp[i][j] = dp[i][j] || dp[i - 1][j];
34                    }
35                }
36            }
37        }
38
39        return dp[m][n];
40    }
41}