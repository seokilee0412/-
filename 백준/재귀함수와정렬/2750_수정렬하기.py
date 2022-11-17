import sys
input = sys.stdin.readline
from copy import deepcopy
N = int(input())
problem = [int(input()) for _ in range(N)]

# not recurssion
problem.sort()
for p in problem:
    print(p)


# recurssion
def recurssion(idx):
    if idx == N-1:
        return
    else:
        if problem[idx] > problem[idx+1]:
            front = deepcopy(problem[idx])
            back = deepcopy(problem[idx+1])
            problem[idx+1] = front
            problem[idx] = back
            recurssion(idx + 1)
            recurssion(idx)
        recurssion(idx + 1)
recurssion(0)

for p in problem:
    print(p)