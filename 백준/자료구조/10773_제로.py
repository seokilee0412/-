import sys
input = sys.stdin.readline

K = int(input())

numbers = [int(input().strip()) for _ in range(K)]
result = []
for n in numbers:
    if n == 0:
        result.pop()
    else:
        result.append(n)

print(sum(result))