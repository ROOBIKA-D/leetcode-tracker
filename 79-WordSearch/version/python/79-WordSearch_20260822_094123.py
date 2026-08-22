# Last updated: 8/22/2026, 9:41:23 AM
1class Solution:
2    def exist(self, board, word):
3
4        rows = len(board)
5        cols = len(board[0])
6
7        def dfs(r, c, index):
8
9            # Entire word found
10            if index == len(word):
11                return True
12
13            # Out of bounds
14            if r < 0 or r >= rows or c < 0 or c >= cols:
15                return False
16
17            # Wrong character
18            if board[r][c] != word[index]:
19                return False
20
21            # Mark current cell as visited
22            temp = board[r][c]
23            board[r][c] = "#"
24
25            # Try all 4 directions
26            found = (
27                dfs(r + 1, c, index + 1) or
28                dfs(r - 1, c, index + 1) or
29                dfs(r, c + 1, index + 1) or
30                dfs(r, c - 1, index + 1)
31            )
32
33            # Backtrack: restore the cell
34            board[r][c] = temp
35
36            return found
37
38        for r in range(rows):
39            for c in range(cols):
40                if board[r][c] == word[0]:
41                    if dfs(r, c, 0):
42                        return True
43
44        return False