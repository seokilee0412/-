n, m = map(int, input().split())

d = [1] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] * i

upper = d[n]
down = d[m] * d[n-m]

print(int(upper//down))