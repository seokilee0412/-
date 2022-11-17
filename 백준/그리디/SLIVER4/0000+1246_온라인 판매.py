N, M = map(int, input().split())
wanted_price = [int(input()) for _ in range(M)]
wanted_price.sort()

p_idx = 0
max_revenue = 0
max_price = 0
sell_amount = 0


for p in wanted_price:
    revenue = p * (len(wanted_price) - p_idx)
    if max_revenue < revenue:
        max_revenue = revenue
        max_price = p
        sell_amount = (len(wanted_price) - p_idx)
        p_idx += 1
    else:
        p_idx += 1
    #     break
if  sell_amount > N:
    max_price = wanted_price[-N]
    max_revenue = wanted_price[-N] * N ###이 단락에서 실패!!! => sell_amount가 N보다 클 때 wanted_price[-N]의 가격으로 N개 만큼 파는 것이 항상 높진 않음 -> 
                                        #2개를 팔 때 [1,1,1,10] 일경우 이 코드대로면 1의 가격으로 2만큼 이익을 얻지만 10의 가격으로 하나만큼 파는 것이 더 이득임...

print(max_price, max_revenue)

N, M = map(int, input().split())
li = sorted([int(input()) for _ in range(M)])
max_p = max_b = 0
for i in range(M):
    t = li[i] * ((M-i) if M-i <= N else N)
    if max_b < t:
        max_b = t
        max_p = li[i]
print(max_p, max_b)