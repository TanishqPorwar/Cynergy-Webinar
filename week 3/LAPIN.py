# https://www.codechef.com/problems/LAPIN

from collections import Counter

for _ in range(int(input())):
    s = input().rstrip()
    n = len(s)
    mid = n//2
    mid2 = n//2
    if n % 2 != 0:
        mid += 1
    c1 = Counter(s[:mid])
    c2 = Counter(s[mid2:])
    if c1 == c2:
        print("YES")
    else:
        print("NO")
