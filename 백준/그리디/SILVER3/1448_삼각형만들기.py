from itertools import combinations
N = int(input())
triangle = [int(input()) for _ in range(N)]

com = combinations(triangle, 3)
result = []
for c in com:
    c = list(c)
    c.sort(reverse=True)
    if c[0] < c[1] + c[2]:
        result.append(c[0] + c[1] + c[2])
    else:
        result.append(-1)

print(max(result))    

import sys
t = int(input())
s = []
for i in range(t):
    s.append(int(sys.stdin.readline()))
s.sort(reverse=True)
istrue = False
for i in range(len(s) - 2):
    if s[i] < s[i + 1] + s[i + 2]:
        print(s[i] + s[i + 1] + s[i + 2])
        istrue = True
        break
if istrue == False:
    print(-1)