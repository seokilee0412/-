import sys
input = sys.stdin.readline

N = int(input())

command = [input().split() for _ in range(N)]
result = []
for c in command:
    if len(c) > 1:
        result.append(c[1])
    else:
        if c[0] == 'pop':
            if len(result) != 0:
                num = result.pop()
                print(num)
            else:
                print(-1)
        elif c[0] == 'size':
            print(len(result))
        
        elif c[0] == 'empty':
            if len(result):
                print(0)
            else:
                print(1)
        
        elif c[0] == 'top':
            if len(result):
                print(result[-1])
            else:
                print(-1)
