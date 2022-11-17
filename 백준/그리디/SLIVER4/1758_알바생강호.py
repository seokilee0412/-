N = int(input())
tip = [int(input()) for _ in range(N)]

tip.sort(reverse=True)
result = 0
for t_idx, t in enumerate(tip):
    ts = max( t - t_idx, 0)
    if ts == 0:
        break
    result += ts

print(result)

