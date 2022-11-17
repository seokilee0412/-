T = int(input())

N = [int(input()) for _ in range(T)]

max_n = max(N)
array = list(range(max_n + 1))

array[0] = 0
array[1] = 0
result = []
for i in range(2, len(array)):
    if array[i] != 0:
        is_right = True
        for k in range(2, int(array[i] ** (0.5)) + 1):
            if array[i] % k == 0:
                is_right = False
                break
        if is_right:
            result.append(array[i])
            for a in range(len(array), array[i]):
                if array[a] != array[i]:
                    array[a] = 0

for n in N:
    minimu = 1e10
    for i in range(len(result)):
        if n//2 < result[i]:
            break
        if n - result[i] in result:
            f = result[i]
            s = n - result[i]
            if minimu > abs(f-s):
                minimu = abs(f-s)
                if f>s:
                    answer = [s, f]
                else:
                    answer = [f,s]
    print(answer[0], answer[1])


