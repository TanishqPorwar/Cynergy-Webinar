# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/long-atm-queue-3/

c = 0
prev = float('inf')


def count(x):
    x = int(x)
    global c, prev
    # print(x, prev)
    if x < prev:
        c += 1
    prev = x


n = int(input())
list(map(count, input().rstrip().split()))
print(c)

# c = 0
# prev = float('inf')
# n = int(input())
# a = list(map(int, input().rstrip().split()))
# for i in a:
#     if i < prev:
#         c += 1
#     prev = i
# print(c)
