# https://www.codechef.com/problems/COPS

for _ in range(int(input())):
    m, x, y = map(int, input().split())
    # print(m, x, y)
    a = list(map(int, input().split()))
    a = [1]+sorted(a)+[100]
    safe = 0
    N = len(a)
    radius = x*y
    for i in range(1, N-1):
        if i == 1:
            temp = a[i] - a[i-1] - radius
            safe += (temp >= 0) * temp
            temp = (a[i+1]-a[i]-2*radius-1)
        elif i == N-2:
            temp = a[i+1]-a[i] - radius
        else:
            temp = (a[i+1]-a[i]-2*radius-1)
        safe += (temp >= 0) * temp
    print(safe)
