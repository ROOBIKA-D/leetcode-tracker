# Last updated: 8/22/2026, 9:19:15 AM
1class Solution:
2    def divide(self, dividend, divisor):
3        INT_MAX = 2**31 - 1
4        INT_MIN = -2**31
5
6        # Special overflow case
7        if dividend == INT_MIN and divisor == -1:
8            return INT_MAX
9
10        # Determine the sign
11        negative = (dividend < 0) != (divisor < 0)
12
13        # Convert both to positive
14        dividend = abs(dividend)
15        divisor = abs(divisor)
16
17        quotient = 0
18
19        # Find how many times divisor fits into dividend
20        while dividend >= divisor:
21            temp = divisor
22            multiple = 1
23
24            while dividend >= temp + temp:
25                temp = temp + temp
26                multiple = multiple + multiple
27
28            dividend = dividend - temp
29            quotient = quotient + multiple
30
31        # Apply sign
32        if negative:
33            quotient = -quotient
34
35        # 32-bit range check
36        if quotient > INT_MAX:
37            return INT_MAX
38
39        if quotient < INT_MIN:
40            return INT_MIN
41
42        return quotient