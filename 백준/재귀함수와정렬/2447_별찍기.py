import sys
input = sys.stdin.readline

N = int(input())

# 10 ~ 18 => N/3 + 1 ~ 2N/3 => N/3 +1 ~ 2N/3 + 1

result = [['*'] * N for _ in range(N)]

def recurssion(n, start_row, start_col):
    if n == 1:
        return
    else:
        for i in range(int(n/3), int(2*n/3)):
            result[start_row + i][start_col + int(n/3) : start_col + int(2 * n/3)] = [' '] * int(n/3)
        for i in range(0, n, int(n/3)):
            for j in range(i, n, int(n/3)):
                recurssion(int(n/3), start_row + i, start_col + j)
                recurssion(int(n/3), start_row + j, start_col + i)

recurssion(N, 0, 0)
results = []
for r in result:
    results.append(''.join(r))
print('\n'.join(results))