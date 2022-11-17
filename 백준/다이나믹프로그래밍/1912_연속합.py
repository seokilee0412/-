import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

d = deepcopy(numbers)

for i in range(1, len(d)):
    d[i] = max(d[i], d[i] + d[i-1])

print(max(d))