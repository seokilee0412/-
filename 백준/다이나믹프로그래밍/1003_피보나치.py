from collections import defaultdict

N = int(input())
num = [int(input()) for _ in range(N)]
max_n = max(num)
d = [-1] * max_n
dictionary = defaultdict(dict)
dictionary[0] = {0:1, 1:0}
dictionary[1] = {0:0, 1:1}
for i in range(2, max_n + 1):
    dictionary[i][0] = dictionary[i-2][0] + dictionary[i-1][0]
    dictionary[i][1] = dictionary[i-2][1] + dictionary[i-1][1]

for n in num:
    print(dictionary[n][0], dictionary[n][1])

