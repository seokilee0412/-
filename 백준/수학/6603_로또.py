import sys
input = sys.stdin.readline
from itertools import combinations
ks = []

while True:
    T = list(map(int, input().split()))
    K, k_list = T[0], T[1:]
    if K == 0:
        break
    else:
        ks.append([K, k_list])
for k,k_list in ks:
    lotto_list = list(combinations(k_list, 6))
    for l in lotto_list:
        print(*l)
    if k_list != ks[-1][1]:
        print()