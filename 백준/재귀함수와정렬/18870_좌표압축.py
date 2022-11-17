import sys
from copy import deepcopy
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

sorted_numbers = sorted(list(set(numbers)))
num_idx = defaultdict()

for idx, n in enumerate(sorted_numbers):
    num_idx[n] = idx

result = []
for n in numbers:
    result.append(num_idx[n])

print(*result)

