# https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array/0

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    c = 0
    b = []
    for i in range(n):
        if a[i] == 0:
            c += 1
        else:
            b.append(a[i])
    b = b+[0]*c
    print(*b)
