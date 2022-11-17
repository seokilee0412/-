import sys
input = sys.stdin.readline
from itertools import combinations

N,M = map(int, input().split())

list_n = list(range(1, N+1))

list_combi = list(combinations(list_n, M))

for l in list_combi:
    print(*l)