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
        if com == 'push_front':
            queue.insert(0, num)
        
        if com == 'push_back':
            queue.append(num)

    else:
        if c == 'pop_front':
            if queue:
                print(queue.popleft())
            else:
                print(-1)

        elif c == 'pop_back':
            if queue:
                print(queue.pop())
            else:
                print(-1)
        
        elif c == 'size':
            print(len(queue))

        elif c == 'empty':
            if not queue:
                print(1)
            else:
                print(0)

        elif c =='front':
            if queue:
                print(queue[0])
            else:
                print(-1)

        elif c == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)