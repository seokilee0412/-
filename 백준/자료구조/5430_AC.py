import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    command = input().rstrip()
    N = int(input())
    numbers = sys.stdin.readline().rstrip()[1:-1].split(",")
    numbers = deque(numbers)
    if N == 0:
        numbers = deque()
    is_popleft = True
    is_error = False
    
    for c in command:
        if c == 'R':
            is_popleft = not is_popleft
        
        elif c == 'D':
            if is_popleft:
                if numbers:
                    numbers.popleft()
                else:
                    is_error = True
                    print('error')
                    break
            else:
                if numbers:
                    numbers.pop()
                else:
                    is_error = True
                    print('error')
                    break
    numbers = list(numbers)

    if not is_error:
        if is_popleft:
            print('[' + ','.join(numbers) + ']')
        else:
            numbers.reverse()
            print('[' + ','.join(numbers) + ']')
