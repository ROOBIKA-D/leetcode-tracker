# Last updated: 8/22/2026, 10:01:10 AM
1class Solution:
2    def maxDepth(self, root):
3
4        if root is None:
5            return 0
6
7        left = self.maxDepth(root.left)
8        right = self.maxDepth(root.right)
9
10        return 1 + max(left, right)