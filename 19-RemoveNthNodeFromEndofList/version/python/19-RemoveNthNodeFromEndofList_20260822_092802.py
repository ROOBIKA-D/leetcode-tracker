# Last updated: 8/22/2026, 9:28:02 AM
1class Solution:
2    def removeNthFromEnd(self, head, n):
3
4        dummy = ListNode(0)
5        dummy.next = head
6
7        slow = dummy
8        fast = dummy
9
10        # Move fast n steps ahead
11        for _ in range(n):
12            fast = fast.next
13
14        # Move both until fast reaches the last node
15        while fast.next:
16            slow = slow.next
17            fast = fast.next
18
19        # Remove the nth node
20        slow.next = slow.next.next
21
22        return dummy.next