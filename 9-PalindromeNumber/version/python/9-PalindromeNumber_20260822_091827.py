# Last updated: 8/22/2026, 9:18:27 AM
1class Solution:
2    def isPalindrome(self, x):
3        if x < 0:
4            return False
5
6        original = x
7        reverse = 0
8
9        while x > 0:
10            digit = x % 10
11            x = x // 10
12
13            reverse = reverse * 10 + digit
14
15        return original == reverse