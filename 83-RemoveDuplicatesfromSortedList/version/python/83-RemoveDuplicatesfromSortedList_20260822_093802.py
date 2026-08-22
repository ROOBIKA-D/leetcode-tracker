# Last updated: 8/22/2026, 9:38:02 AM
1class Solution:
2    def deleteDuplicates(self, head):
3
4        current = head
5
6        while current and current.next:
7
8            if current.val == current.next.val:
9                current.next = current.next.next
10            else:
11                current = current.next
12
13        return head