# Last updated: 8/22/2026, 9:29:38 AM
1class Solution:
2    def searchRange(self, nums, target):
3
4        def findFirst():
5            left = 0
6            right = len(nums) - 1
7            result = -1
8
9            while left <= right:
10                mid = (left + right) // 2
11
12                if nums[mid] == target:
13                    result = mid
14                    right = mid - 1
15                elif nums[mid] < target:
16                    left = mid + 1
17                else:
18                    right = mid - 1
19
20            return result
21
22        def findLast():
23            left = 0
24            right = len(nums) - 1
25            result = -1
26
27            while left <= right:
28                mid = (left + right) // 2
29
30                if nums[mid] == target:
31                    result = mid
32                    left = mid + 1
33                elif nums[mid] < target:
34                    left = mid + 1
35                else:
36                    right = mid - 1
37
38            return result
39
40        return [findFirst(), findLast()]