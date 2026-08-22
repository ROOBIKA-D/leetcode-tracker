# Last updated: 8/22/2026, 9:49:47 AM
1class Solution:
2    def strStr(self, haystack, needle):
3
4        for i in range(len(haystack) - len(needle) + 1):
5
6            if haystack[i:i + len(needle)] == needle:
7                return i
8
9        return -1