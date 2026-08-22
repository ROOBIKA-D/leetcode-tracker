# Last updated: 8/22/2026, 9:26:44 AM
1class Solution:
2    def combinationSum(self, candidates, target):
3        result = []
4
5        def backtrack(start, current, total):
6            if total == target:
7                result.append(current[:])
8                return
9
10            if total > target:
11                return
12
13            for i in range(start, len(candidates)):
14                current.append(candidates[i])
15
16                # i, not i + 1, because we can reuse the same number
17                backtrack(i, current, total + candidates[i])
18
19                current.pop()
20
21        backtrack(0, [], 0)
22
23        return result