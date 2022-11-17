import sys
input = sys.stdin.readline

A = int(input())

array = list(map(int, input().split()))

d = [1] * A

for i in range(1,A):
    for j in range(0, i):
        if array[i] < array[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))