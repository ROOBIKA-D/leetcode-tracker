# Last updated: 8/22/2026, 9:46:48 AM
1class Solution:
2    def isValid(self, s):
3        stack = []
4
5        pairs = {
6            ')': '(',
7            ']': '[',
8            '}': '{'
9        }
10
11        for char in s:
12
13            if char in '([{':
14                stack.append(char)
15
16            else:
17                if not stack or stack[-1] != pairs[char]:
18                    return False
19
20                stack.pop()
21
22        return len(stack) == 0