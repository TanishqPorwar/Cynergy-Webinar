# https://practice.geeksforgeeks.org/problems/remove-duplicates/0

from collections import defaultdict
for _ in range(int(input())):
    s = input().rstrip()
    d = defaultdict(lambda: False)
    s2 = ""
    for i in s:
        if d[i] == False:
            s2 += i
            d[i] = True
    print(s2)
