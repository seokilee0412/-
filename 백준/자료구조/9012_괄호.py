import sys
input = sys.stdin.readline

T = int(input())

command = [input().strip() for _ in range(T)]

for cs in command:
    result = []
    for c in cs:
        if len(result):
            cri = result[-1]
            if cri == '(' and c == ')':
                result.pop()
            else:
                result.append(c)
        else:
            result.append(c)
    if len(result):
        print('NO')
    else:
        print('YES')
