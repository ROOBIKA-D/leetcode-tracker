// Last updated: 8/22/2026, 11:55:53 AM
1var checkDivisibility = function(n) {
2    let num = n;
3    let digitSum = 0;
4    let digitProduct = 1;
5
6    while (num > 0) {
7        let digit = num % 10;
8
9        digitSum += digit;
10        digitProduct *= digit;
11
12        num = Math.floor(num / 10);
13    }
14
15    let total = digitSum + digitProduct;
16
17    return n % total === 0;
18};