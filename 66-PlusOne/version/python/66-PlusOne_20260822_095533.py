# Last updated: 8/22/2026, 9:55:33 AM
1class Solution:
2    def plusOne(self, digits):
3
4        for i in range(len(digits) - 1, -1, -1):
5
6            if digits[i] < 9:
7                digits[i] += 1
8                return digits
9
10            digits[i] = 0
11
12        return [1] + digits