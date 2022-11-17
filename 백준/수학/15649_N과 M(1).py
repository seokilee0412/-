from itertools import permutations

N, M = map(int, input().split())

array = list(range(1, N + 1 ))

result = list(permutations(array, M))

for r in result:
    print(*r)