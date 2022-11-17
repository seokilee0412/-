N = []
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    else:
        N.append([L,P, V])

for i in range(len(N)):
    L = N[i][0]
    P = N[i][1]
    V = N[i][2]
    value = (V//P) * L
    # val = V  - ((V//P) * P)
    val  = min(V%P, L)
    value += val
    print(f'Case {i + 1}: {value}')

    # 19 4 2
    # 3
    # 2