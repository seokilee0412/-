import sys

input = sys.stdin.readline
N = int(input())

# 47 -1 / 2 = 23
# 5 -1 /2 = 2 ** * ** (2)

# 밑 별 3개씩 줌
num = int(N//3)

matrix = [[' ']*2*N for _ in range(N)]

def recursion(row, col, size):
    if size == 3:
        matrix[row][col] = '*'
        matrix[row + 1][col - 1] = matrix[row + 1][col + 1] = "*"
        for k in range(-2, 3):
            matrix[row + 2][col - k] = "*"
    
    else:
        newSize = size//2
        recursion(row, col, newSize)
        recursion(row + newSize, col - newSize, newSize)
        recursion(row + newSize, col + newSize, newSize)

recursion(0, N - 1, N)
for m in matrix:
    print("".join(m))