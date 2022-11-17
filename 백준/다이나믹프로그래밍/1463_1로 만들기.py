N = int(input())

d = [1e10] * (N+1)
if len(d) == 1:
    d[0] =1
elif len(d) == 2:
    d[0],d[1] = 0,0
else:
    d[0], d[1], d[2] = 0, 0, 1
for i in range(3, N+1):
    if i%3 == 0:
        d[i] = min(d[i], d[int(i//3)] + 1)
    if i%2 == 0:
        d[i] = min(d[i], d[int(i//2)] + 1)
    d[i] = min(d[i], d[i-1] + 1)

print(d[N])
