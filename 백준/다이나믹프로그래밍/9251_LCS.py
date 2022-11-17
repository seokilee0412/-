import sys
input = sys.stdin.readline

first = input().strip()
second = input().strip()

d = [[0] * (len(second)+ 1) for _ in range(len(first)+1)]
start = 0
for i in range(1, len(first) + 1):
    for j in range(1, len(second) +1):
        if first[i-1] == second[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])
        
print(d[-1][-1])