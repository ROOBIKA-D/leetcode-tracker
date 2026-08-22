# Last updated: 8/22/2026, 9:54:38 AM
1class Solution:
2    def numDecodings(self, s):
3        n = len(s)
4
5        dp = [0] * (n + 1)
6
7        dp[0] = 1
8
9        # First character
10        if s[0] != '0':
11            dp[1] = 1
12
13        for i in range(2, n + 1):
14
15            # Take one digit
16            if s[i - 1] != '0':
17                dp[i] += dp[i - 1]
18
19            # Take two digits
20            two_digit = int(s[i - 2:i])
21
22            if 10 <= two_digit <= 26:
23                dp[i] += dp[i - 2]
24
25        return dp[n]