# import sys
# from copy import deepcopy
# from collections import defaultdict
# input = sys.stdin.readline

# N = int(input())

# t_p_list = [[0,0]]
# t_p_list.extend([list(map(int, input().split())) for _ in range(N)])

# d = [0] * (N+1)
# dictionary = defaultdict(list)

# for i in range(1, N+1):
#     candi = []
#     if t_p_list[i][0] + i > N + 1:
#         break
    
#     for j in range(i, 0, -1):
#         if t_p_list[j][0] + j <= i:
#             candi.append(j)

#         else:
#             continue
#     d[i] = t_p_list[i][1]
#     for c in candi:
#         d[i] = max(d[i], d[c] + t_p_list[i][1], t_p_list[i][1])

    
# print(max(d))

import sys
input = sys.stdin.readline

N = int(input())
time_price_list = []
for _ in range(N):
    time_price_list.append(list(map(int, input().split())))
d = [0] * (N+1)

for i in range(N):
    if d[i] < d[i-1]:
            d[i] = d[i-1]
    if i + time_price_list[i][0] <= N:
        d[i + time_price_list[i][0]] = max(d[i + time_price_list[i][0]], d[i] + time_price_list[i][1])

print(max(d))