# Last updated: 8/22/2026, 9:53:39 AM
1class Solution:
2    def permute(self, nums):
3        result = []
4
5        def backtrack(path, used):
6            # All numbers are selected
7            if len(path) == len(nums):
8                result.append(path[:])
9                return
10
11            for i in range(len(nums)):
12                if used[i]:
13                    continue
14
15                # Choose
16                path.append(nums[i])
17                used[i] = True
18
19                # Explore
20                backtrack(path, used)
21
22                # Undo choice
23                path.pop()
24                used[i] = False
25
26        backtrack([], [False] * len(nums))
27
28        return result