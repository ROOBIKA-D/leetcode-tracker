# Last updated: 8/22/2026, 9:39:09 AM
1class Solution:
2    def lengthOfLastWord(self, s):
3        i = len(s) - 1
4
5        # Skip spaces at the end
6        while s[i] == ' ':
7            i -= 1
8
9        count = 0
10
11        # Count the last word
12        while i >= 0 and s[i] != ' ':
13            count += 1
14            i -= 1
15
16        return count