import sys
input = sys.stdin.readline
from itertools import combinations
N,S = map(int, input().split())
num = list(map(int, input().split()))
count = 0
for i in range(1,len(num) + 1):
    combi = list(combinations(num, i))
    sum_combi = [True if sum(c) == S else False for c in combi]
    count+= sum(sum_combi)

print(count)