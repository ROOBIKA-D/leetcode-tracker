# Last updated: 8/22/2026, 9:20:18 AM
1class Solution:
2    def mySqrt(self, x):
3        if x < 2:
4            return x
5
6        left = 1
7        right = x // 2
8        answer = 0
9
10        while left <= right:
11            mid = (left + right) // 2
12
13            if mid * mid <= x:
14                answer = mid
15                left = mid + 1
16            else:
17                right = mid - 1
18
19        return answer