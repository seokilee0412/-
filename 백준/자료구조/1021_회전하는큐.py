import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
position = list(map(int, input().split()))
queue = deque(list(range(1, N+1)))
count = 0
for p in position:
    while True:
        if queue[0] == p:
            queue.popleft()
            break
        else:
            if queue.index(p) < len(queue)/2:
                queue.append(queue.popleft())
                count += 1
            else:
                queue.appendleft(queue.pop())
                count += 1
print(count)