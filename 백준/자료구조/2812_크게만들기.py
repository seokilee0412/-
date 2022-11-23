import sys

input = sys.stdin.readline

N, K = map(int, input().split())
numbers = input().rstrip()
stack = []
stop = K
for i in range(N):
    while stop > 0 and stack and stack[-1] < numbers[i]:
        stack.pop()
        stop -= 1
    stack.append(numbers[i])

print(''.join(stack[:N-K]))