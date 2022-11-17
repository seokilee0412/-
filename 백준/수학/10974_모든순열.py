from itertools import permutations

N = int(input())

list_n = list(range(1, N+1))

list_combi = permutations(list_n, N)
result = set()
for l in list_combi:
    if l not in result:
        print(*l)
        result.add(l)

