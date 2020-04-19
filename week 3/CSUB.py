# https://www.codechef.com/problems/CSUB

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    count = s.count('1')
    print((count*(count+1))//2)
