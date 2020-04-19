import os
import sys


def check(mid, n):
    for i in range(mid, n+1):
        for j in range(mid, n+1):
            tmp = c[i][j] - c[i-mid][j-mid]
            if tmp < k:
                return True
    return False

# Complete the substringDiff function below.


def substringDiff(k, s1, s2):
    n = len(s1)
    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                c[i+1][j+1] = c[i][j]
            else:
                c[i+1][j+1] = c[i][j]+1
    low = 0
    high = n
    while(low < high):
        mid = (low+high+1)//2
        if (check(mid, n)):
            low = mid
        else:
            high = mid - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        kS1S2 = input().split()

        k = int(kS1S2[0])

        s1 = kS1S2[1]

        s2 = kS1S2[2]

        n = len(s1)

        c = [[0 for i in range(n)] for j in range(n)]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
