# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# W = dict()

# for _ in range(N):
#     w,v = map(int, input().split())
#     W[w] = v
    
# d = [0] * (K + 1)

# for i in range(1, K +1 ):
#     for j in (0, int(i//2) + 1):
#         if W[i-j] == 1 and W[j] == 1:
#             d[i] = max(d[i], W[i-j] + W[j])

# print(d[K])


import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight_value_list = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * (K+1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = weight_value_list[i-1][0]
        v = weight_value_list[i-1][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)

print(d[N][K])