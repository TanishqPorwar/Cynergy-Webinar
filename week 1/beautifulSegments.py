# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/beautiful-segments/


for _ in range(int(input())):
    n = int(input())
    count = 0
    if n:
        a = list(map(int, input().split()))
        k1, k2, flag = 0, 0, 0
        for i in range(n-1):
            if a[i+1] >= a[i] and flag == 2:
                # print("update")
                flag = 1
                if k1 == k2:
                    count += k1
                else:
                    count += min(k1, k2)
                # print(count)
                k1, k2 = 1, 0

            elif a[i+1] < a[i]:
                # print("fall")
                k2 += 1
                flag = 2
            elif a[i] <= a[i+1]:
                # print("rise")
                flag = 1
                k1 += 1
            elif a[i+1] < a[i] and flag == 2:
                # print("fall2")
                k2 += 1

        if flag == 2:
            if k1 == k2:
                count += k1
            else:
                count += min(k1, k2)
    print(count)
