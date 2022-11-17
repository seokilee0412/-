
# max_karloe_per_price = 0
# for t_k_idx in range(1, len(toping_karloe) + 1):
#     total_karloe = dou_karloe + sum([ toping_karloe[i] for i in range(len(toping_karloe[:t_k_idx]))])
#     karloe_per_price = int(  (total_karloe ) // ( t_k_idx * price_toping + price_dou))
#     if karloe_per_price > max_karloe_per_price:
#         max_karloe_per_price = karloe_per_price
# print(max_karloe_per_price)

# 500/14
# 600/16 37.5
# 650/18
N = int(input())
price_dou, price_toping = map(int, input().split())
dou_karloe = int(input())
toping_karloe = [int(input()) for _ in range(N)]

toping_karloe.sort(reverse=True)
total_karloe = dou_karloe
total_price = price_dou
idx = 0
max_karloe_per_price = 0
for idx in range(len(toping_karloe)):
    total_karloe += toping_karloe[idx]
    total_price += price_toping
    if int(total_karloe / total_price) > max_karloe_per_price:
        max_karloe_per_price = int(total_karloe / total_price)

print(max_karloe_per_price)

import sys

read = lambda: sys.stdin.readline().rstrip()

N = int(read())
A, B = map(int, read().split())
C = int(read())
D = []

for _ in range(N):
    D.append(int(read()))

D.sort(reverse=True)

answer = C / A

for i in range(1, len(D)+1):
    calorie = C + sum(D[0:i])
    price = A + (B * i)

    if calorie / price > answer:
        answer = calorie / price
    else:
        break

print(int(answer))