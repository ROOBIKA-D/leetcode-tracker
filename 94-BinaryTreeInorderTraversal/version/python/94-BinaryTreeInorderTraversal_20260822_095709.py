# Last updated: 8/22/2026, 9:57:09 AM
1class Solution:
2    def inorderTraversal(self, root):
3        result = []
4
5        def inorder(node):
6            if node is None:
7                return
8
9            inorder(node.left)
10            result.append(node.val)
11            inorder(node.right)
12
13        inorder(root)
14        return result