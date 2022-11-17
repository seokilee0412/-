import sys
input = sys.stdin.readline
T = int(input())

num = [int(input()) for _ in range(T)]
max_n = max(num)
d = [1] * (max_n + 1)
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, max_n + 1):
    d[i] = d[i-3] + d[i-2] + d[i-1]

for n in num:
    print(d[n])
