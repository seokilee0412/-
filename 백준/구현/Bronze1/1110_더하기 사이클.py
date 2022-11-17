N = input()
if len(N) == 1:
    N = '0' + N
result = ''
cnt = 0
while result != N:
    if result == '':
        result = N
    if len(result) == 1:
        result = '0' + result
    sum_ = str(int(result[0]) + int(result[1]))
    if len(sum_) == 1:
        sum_ = '0' + sum_
    result = result[1] + sum_[1]
    cnt += 1

print(cnt)