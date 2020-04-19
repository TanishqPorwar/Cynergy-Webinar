# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/pairs-having-similar-element-eed098aa/
def nc2(m):
    return m*(m+1)/2


def SimilarElementsPairs(a, N):
    a.sort()
    count = 0
    k = 0
    flag = 0
    for i in range(N-1):
        if a[i+1]-a[i] == 1:
            k += 1
            flag = 1
        if a[i+1] == a[i]:
            k += 1
        if a[i+1]-a[i] > 1 or i == N-2:
            if flag:
                count += nc2(k)
                flag = 0
            k = 0
        # print(k, end=" ")
    return count


N = int(input())
A = list(map(int, input().split()))
out_ = SimilarElementsPairs(A, N)
print(int(out_))
