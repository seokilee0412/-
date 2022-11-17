import sys
input = sys.stdin.readline

N = int(input())

MATRIX = [list(map(int, input().split())) for _ in range(N)]

one_count = 0
zero_count = 0
def recurssion(n, matrix):
    global one_count
    global zero_count
    if n==1:
        if matrix[0][0] == 1:
            one_count += 1
        elif matrix[0][0] == 0:
            zero_count += 1
    else:
        if matrix == [[1] * len(matrix[0])] * len(matrix[1]):
            one_count += 1
        elif matrix == [[0] * len(matrix[0])] * len(matrix[1]):
            zero_count += 1
        else:
            recurssion(int(n/2), [a[:int(n/2)] for a in matrix[:int(n/2)]])
            recurssion(int(n/2), [a[int(n/2):] for a in matrix[:int(n/2)]])
            recurssion(int(n/2), [a[int(n/2):] for a in matrix[int(n/2):]])
            recurssion(int(n/2), [a[:int(n/2)] for a in matrix[int(n/2):]])


recurssion(N, MATRIX)
print(zero_count)
print(one_count)