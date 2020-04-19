# https://www.hackerrank.com/challenges/array-left-rotation/problem

nd = input().split()
n = int(nd[0])
d = int(nd[1])
d = d % n
# print(d)
a = list(map(int, input().rstrip().split()))
a = a[d:]+a[:d]
print(*a)
