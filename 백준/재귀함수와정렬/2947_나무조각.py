import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
def check_num(num, i):
    if num[i] > num[i+1]:
        num[i], num[i+1] = num[i+1], num[i]
        print(*num)

while True:
    if numbers == [1,2,3,4,5]:
        break
    else:
        for i in range(4):
            check_num(numbers, i)