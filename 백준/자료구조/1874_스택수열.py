import sys
input = sys.stdin.readline

N = int(input())
correct = [int(input()) for _ in range(N)]

stack = []
result = []
last = 0
for cs in correct:
    if len(stack) == 0:
        for c in range(last + 1, cs + 1):
            stack.append(c)
            result.append('+')
        result.append('-')

        last_now = stack.pop()
        if last_now > last:
            last = last_now
    elif stack[-1] < cs:
        for c in range(last + 1, cs + 1):
            stack.append(c)
            result.append('+')
        result.append('-')
        last_now = stack.pop()
        if last_now > last:
            last = last_now
    else:
        if stack[-1] != cs:
            result = 'NO'
            break
        else:
            last_now = stack.pop()
            if last_now > last:
                last = last_now
            result.append('-')

if result != 'NO':
    for r in result:
        print(r)
else:
    print('NO')
