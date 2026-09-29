// Last updated: 9/29/2026, 3:01:46 PM
1var hasValidPath = function(grid) {
2    const m = grid.length;
3    const n = grid[0].length;
4
5    if ((m + n - 1) % 2 !== 0) return false;
6    if (grid[0][0] === ')') return false;
7
8    const dp = Array.from({ length: m }, () =>
9        Array.from({ length: n }, () => new Set())
10    );
11
12    dp[0][0].add(1);
13
14    for (let i = 0; i < m; i++) {
15        for (let j = 0; j < n; j++) {
16            if (i === 0 && j === 0) continue;
17
18            const change = grid[i][j] === '(' ? 1 : -1;
19
20            if (i > 0) {
21                for (const balance of dp[i - 1][j]) {
22                    const newBalance = balance + change;
23                    if (newBalance >= 0) {
24                        dp[i][j].add(newBalance);
25                    }
26                }
27            }
28
29            if (j > 0) {
30                for (const balance of dp[i][j - 1]) {
31                    const newBalance = balance + change;
32                    if (newBalance >= 0) {
33                        dp[i][j].add(newBalance);
34                    }
35                }
36            }
37        }
38    }
39
40    return dp[m - 1][n - 1].has(0);
41};