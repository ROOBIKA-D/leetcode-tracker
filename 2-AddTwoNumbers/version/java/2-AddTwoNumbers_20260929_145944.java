// Last updated: 9/29/2026, 2:59:44 PM
1class Solution {
2    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
3
4        ListNode dummy = new ListNode(0);
5        ListNode current = dummy;
6
7        int carry = 0;
8
9        while (l1 != null || l2 != null || carry != 0) {
10
11            int sum = carry;
12
13            if (l1 != null) {
14                sum += l1.val;
15                l1 = l1.next;
16            }
17
18            if (l2 != null) {
19                sum += l2.val;
20                l2 = l2.next;
21            }
22
23            int digit = sum % 10;
24            carry = sum / 10;
25
26            current.next = new ListNode(digit);
27            current = current.next;
28        }
29
30        return dummy.next;
31    }
32}