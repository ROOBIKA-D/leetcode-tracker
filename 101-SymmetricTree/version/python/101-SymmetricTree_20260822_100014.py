# Last updated: 8/22/2026, 10:00:14 AM
1class Solution:
2    def isSymmetric(self, root):
3
4        def mirror(left, right):
5            if left is None and right is None:
6                return True
7
8            if left is None or right is None:
9                return False
10
11            if left.val != right.val:
12                return False
13
14            return (
15                mirror(left.left, right.right)
16                and mirror(left.right, right.left)
17            )
18
19        return mirror(root.left, root.right)