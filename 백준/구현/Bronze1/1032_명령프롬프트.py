N = int(input())
cmd = [input() for _ in range(N)]
result = ''
for i in range(len(cmd[0])):
    cri = ''
    count = 0
    for j in range(N):
        if cri != '':
            if cri == cmd[j][i]:
                count +=1
            else:
                result += '?'
                break
        else:
            cri = cmd[j][i]
    if count == len(cmd) - 1:
        result += cri
print(result)