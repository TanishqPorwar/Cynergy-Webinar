# https://www.codechef.com/problems/RAINBOWA

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    if s == s[::-1] and set(s) == {1, 2, 3, 4, 5, 6, 7}:
        print('yes')
    else:
        print("no")
