# hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/can-you-solve-it/

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l1 = [(v-i) for (i, v) in enumerate(a)]
    l2 = [(v+i) for (i, v) in enumerate(a)]
    print(max(max(l1)-min(l1), max(l2)-min(l2)))
