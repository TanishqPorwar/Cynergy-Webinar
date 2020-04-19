# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/

import sys

lines = sys.stdin.readlines()
line_index = -1


def getlines():
    global line_index
    line_index += 1
    return lines[line_index]


nq = getlines().rstrip().split()
a = getlines().rstrip().split()
swap = {'0': '1', '1': '0'}
out = {'1': 'ODD\n', '0': 'EVEN\n'}
for _ in range(int(nq[1])):
    qu = getlines().rstrip().split()
    pos = int(qu[-1])-1
    if qu[0] == '1':
        a[pos] = swap[a[pos]]
    else:
        sys.stdout.write(out[a[pos]])
