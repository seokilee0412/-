N = int(input())

number = list(map(int, input().split()))
count = 0
check_num = []
for n in number:
    is_right = True
    if n == 0 or n ==1:
        continue
    if n !=2 :
        for v in range(2, int(n ** 0.5) + 1):
            if n%v == 0:
                is_right = False
                break
        if is_right:
            count += 1
    else:
        count += 1

print(count)