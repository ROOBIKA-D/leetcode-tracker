# Last updated: 8/22/2026, 9:36:50 AM
1class Solution:
2    def addBinary(self, a, b):
3        i = len(a) - 1
4        j = len(b) - 1
5
6        carry = 0
7        result = []
8
9        while i >= 0 or j >= 0 or carry:
10
11            total = carry
12
13            if i >= 0:
14                total += int(a[i])
15                i -= 1
16
17            if j >= 0:
18                total += int(b[j])
19                j -= 1
20
21            result.append(str(total % 2))
22            carry = total // 2
23
24        return ''.join(result[::-1])