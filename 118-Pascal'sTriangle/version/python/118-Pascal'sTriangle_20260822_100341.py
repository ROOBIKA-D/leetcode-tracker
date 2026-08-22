# Last updated: 8/22/2026, 10:03:41 AM
1class Solution:
2    def generate(self, numRows):
3        result = []
4
5        for i in range(numRows):
6            row = [1] * (i + 1)
7
8            for j in range(1, i):
9                row[j] = result[i - 1][j - 1] + result[i - 1][j]
10
11            result.append(row)
12
13        return result