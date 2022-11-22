import sys

input = sys.stdin.readline

N = int(input())
command = list(map(int, input().split()))
command = list(reversed(command))
result = []
stack = []
for i in range(N):
    while stack:
        if stack[-1][1] > command[i]:
            result.append(stack[-1][1])
            break
        else:
            stack.pop()
    if not stack:
        result.append(-1)
    stack.append([i, command[i]])

result = list(reversed(result))
print(*result)
