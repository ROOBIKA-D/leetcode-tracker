# Last updated: 8/22/2026, 9:21:16 AM
1class Solution:
2    def longestPalindrome(self, s):
3        if len(s) < 2:
4            return s
5
6        start = 0
7        end = 0
8
9        def expand(left, right):
10            while left >= 0 and right < len(s) and s[left] == s[right]:
11                left -= 1
12                right += 1
13
14            return left + 1, right - 1
15
16        for i in range(len(s)):
17
18            # Odd length palindrome
19            left1, right1 = expand(i, i)
20
21            # Even length palindrome
22            left2, right2 = expand(i, i + 1)
23
24            if right1 - left1 > end - start:
25                start = left1
26                end = right1
27
28            if right2 - left2 > end - start:
29                start = left2
30                end = right2
31
32        return s[start:end + 1]