N = int(input())

d = [1] * (N+1)

for i in range(3, N + 1):
    d[i] = d[i-2] + d[i-1]

print(d[N])