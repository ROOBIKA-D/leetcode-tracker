# Last updated: 8/22/2026, 9:16:33 AM
1class Solution:
2    def reverse(self, x):
3        sign = -1 if x < 0 else 1
4        x = abs(x)
5
6        rev = 0
7
8        while x > 0:
9            digit = x % 10
10            x = x // 10
11
12            rev = rev * 10 + digit
13
14        rev = rev * sign
15
16        if rev < -2**31 or rev > 2**31 - 1:
17            return 0
18
19        return rev