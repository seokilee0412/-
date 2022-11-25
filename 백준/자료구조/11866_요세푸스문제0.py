import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque(list(range(1, N + 1)))
result = []
count = 1
while queue:
    now = queue.popleft()
    if count == K:
        result.append(str(now))
        count = 1
    else:
        queue.append(now)
        count += 1


print('<' + ', '.join(result) + '>')