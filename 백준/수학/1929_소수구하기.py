import sys
input = sys.stdin.readline

M, N = map(int, input().split())
array = list(range(N+1))
array[0], array[1] = 0, 0

for num in range(N+1):
    if array[num] != 0:
        is_right = True
        for v in range(2, int(num**0.5) + 1):
            if num%v == 0:
                is_right = False
                break
        if is_right:
            array[num] = num
            for a in range(0, len(array), num):
                if a != num:
                    array[a] = 0
array.sort()
for a in array:
    if a != 0 and a >= M:
        print(a)