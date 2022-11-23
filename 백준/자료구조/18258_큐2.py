import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

command = [input().rstrip() for _ in range(N)]
queue = deque()
for c in command:
    if len(c.split()) > 1:
        com, num = c.split()
        num = int(num)
        if com == 'push':
            queue.append(num)
    else:
        if c == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)

        elif c == 'size':
            print(len(queue))

        elif c == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        
        elif c == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)

        elif c == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)