# https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

n, x = map(int, input().split())
a = list(map(int, input().split()))
p = n
for i in range(n-1):
    if a[i] > a[i+1]:
        p = i
        break
l = p
r = (p+1) % n
count = 0
while l != r:
    if a[l]+a[r] == x:
        count += 1
        if r == (l-1+n) % n:
            break
        l = (l-1+n) % n
        r = (r+1) % n
    elif a[l]+a[r] < x:
        r = (r+1) % n
    else:
        l = (l-1+n) % n
print(count)
