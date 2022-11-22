import sys
input = sys.stdin.readline

command = input().rstrip()

'''
c == '(' 이고 command[idx+1]가 ')'일 때면 레이저이므로 stack의 수만큼 더함
해당 조건이 아닐 경우,
stack에 (를 저장하고 레이저를 만날 때마다 stack의 수를 더하고, 
')'를 만날때마다 하나씩 더함
'''
stack = []
result = 0
for idx, c in enumerate(command):
    if c=='(' and command[idx+1] == ')':
        result += len(stack)
    elif c=='(':
        stack.append(c)
    
    else:
        if idx > 0 and command[idx-1] == '(':
            continue
        else:
            result += 1
            stack.pop()

print(result)
