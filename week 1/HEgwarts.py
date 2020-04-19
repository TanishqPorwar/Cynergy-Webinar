# https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/the-witches-of-hegwarts-1/

from collections import defaultdict

for _ in range(int(input())):
    start = int(input())
    path = defaultdict(lambda: -1)
    q = [start]
    path[start] = 0
    while len(q) != 0:
        cur = q.pop(0)
        # print(cur, end=" ")
        if cur < 1:
            break
        if (cur/2).is_integer() and path[(cur//2)] == -1:
            # print(cur/2, end=" ")
            path[(cur//2)] = path[cur]+1
            q.append(cur//2)
        if (cur/3).is_integer() and path[(cur//3)] == -1:
            # print(cur/3, end=" ")
            path[(cur//3)] = path[cur]+1
            q.append(cur//3)
        if path[cur-1] == -1:
            # print(cur-1, end=" ")
            path[cur-1] = path[cur]+1
            q.append(cur-1)
    print(path[1])
