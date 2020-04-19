# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-welcome-problem/

i = 0


def arrSum(x):
    global i
    C[i] += int(x)
    i += 1


n = int(input())
C = list(map(int, input().split()))
list(map(arrSum, input().split()))
print(*C)
