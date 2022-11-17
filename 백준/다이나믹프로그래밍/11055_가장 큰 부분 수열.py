import sys
# from copy import deepcopy
input = sys.stdin.readline

A = int(input())

array = list(map(int, input().split()))

# d = deepcopy(array)
d= array

for i in range(1,A):
    for j in range(0, i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + array[i])

print(max(d))