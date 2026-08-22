# Last updated: 8/22/2026, 9:45:20 AM
1class Solution:
2    def isSameTree(self, p, q):
3
4        # Both nodes are empty
5        if p is None and q is None:
6            return True
7
8        # One is empty, the other is not
9        if p is None or q is None:
10            return False
11
12        # Values are different
13        if p.val != q.val:
14            return False
15
16        # Check left and right subtrees
17        return (
18            self.isSameTree(p.left, q.left)
19            and self.isSameTree(p.right, q.right)
20        )