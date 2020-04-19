# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/


n = int(input())
a = list(map(int, input().split()[::-1]))
maxi = float('-inf')
out = []
for i in range(n):
    if a[i] >= maxi:
        # print(a[i], end=" ")
        out.append(a[i])
        maxi = a[i]
print(*out[::-1])
