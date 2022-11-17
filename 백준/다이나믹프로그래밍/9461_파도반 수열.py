# f(n) = f(n-3) + f(n-2), d[0] = 1, d[1] = 1, d[2] = 1

T = int(input())
N = [int(input()) for _ in range(T)]

max_n = max(N)
d = [0] * (max_n)
d[0] = 1
d[1] = 1
d[2] = 1

for n in range(3, max_n):
    d[n] = d[n-3] + d[n-2]

for n in N:
    print(d[n-1])