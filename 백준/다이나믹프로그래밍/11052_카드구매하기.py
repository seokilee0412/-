import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
price = [0]
price.extend(list(map(int, input().split())))

d = deepcopy(price)
if N > 1:
    d[2] = price[2] if price[1] * 2 < price[2] else price[1] * 2 
for i in range(2, N + 1):
    maximum = 1e-6
    for j in range(i//2 + 1):
        if j == 0:
            value = price[i]
        else:
            value = d[j] + d[i-j]
        if value > maximum:
            maximum = value
            d[i] = value
print(d[N])