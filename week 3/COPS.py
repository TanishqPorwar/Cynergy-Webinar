# https://www.codechef.com/problems/COPS


for _ in range(int(input())):
    m, x, y = map(int, input().split())
    arr = [True for i in range(0, 101)]
    a = list(map(int, input().split()))
    radius = x*y
    for i in a:
        end = i + radius
        start = i - radius
        if start < 1:
            start = 1
        if end > 100:
            end = 100
        for j in range(start, end+1):
            arr[j] = False

    print(arr.count(True)-1)
