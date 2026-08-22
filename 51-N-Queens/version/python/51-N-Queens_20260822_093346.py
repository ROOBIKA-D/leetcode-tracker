# Last updated: 8/22/2026, 9:33:46 AM
1class Solution:
2    def solveNQueens(self, n):
3        result = []
4
5        board = [["."] * n for _ in range(n)]
6
7        cols = set()
8        diag1 = set()
9        diag2 = set()
10
11        def backtrack(row):
12            # All queens placed
13            if row == n:
14                solution = []
15
16                for r in board:
17                    solution.append("".join(r))
18
19                result.append(solution)
20                return
21
22            for col in range(n):
23
24                # Check if column is already occupied
25                if col in cols:
26                    continue
27
28                # Check diagonals
29                if row - col in diag1:
30                    continue
31
32                if row + col in diag2:
33                    continue
34
35                # Place queen
36                board[row][col] = "Q"
37                cols.add(col)
38                diag1.add(row - col)
39                diag2.add(row + col)
40
41                # Move to next row
42                backtrack(row + 1)
43
44                # Remove queen (backtrack)
45                board[row][col] = "."
46                cols.remove(col)
47                diag1.remove(row - col)
48                diag2.remove(row + col)
49
50        backtrack(0)
51
52        return result